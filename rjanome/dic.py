# -*- coding: utf-8 -*-

# Copyright 2015 moco_beta
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#from __future__ import with_statement
import os
#import io
#import pickle
#import gzip
#from struct import pack, unpack
from .fst import Matcher, create_minimum_transducer, compileFST
#import traceback
import logging
import sys

PY3 = sys.version_info[0] == 3

SYSDIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sysdic")

FILE_FST_DATA = 'fst.data'
# FILE_ENTRIES = 'entries.data'
# FILE_CONNECTIONS = 'connections.data'

MODULE_FST_DATA = 'fstdata.py'
MODULE_ENTRIES = 'entries.py'
MODULE_CONNECTIONS = 'connections.py'
MODULE_CHARDEFS = 'chardef.py'
MODULE_UNKNOWNS = 'unknowns.py'

FILE_USER_FST_DATA = 'user_fst.data'
FILE_USER_ENTRIES_DATA = 'user_entries.data'

def save_fstdata(data, dir='.'):
    _save(os.path.join(dir, FILE_FST_DATA), data, 9)
    # _save_as_module(os.path.join(dir, MODULE_FST_DATA), data)

def save_entries(entries, dir=u'.'):
    #_save(os.path.join(dir, FILE_ENTRIES), pickle.dumps(entries), compresslevel)
    _save_as_module(os.path.join(dir, MODULE_ENTRIES), entries)

def save_connections(connections, dir=u'.'):
    #_save(os.path.join(dir, FILE_CONNECTIONS), pickle.dumps(connections), compresslevel)
    _save_as_module(os.path.join(dir, MODULE_CONNECTIONS), connections)

def save_chardefs(chardefs, dir=u'.'):
    _save_as_module(os.path.join(dir, MODULE_CHARDEFS), chardefs)

def save_unknowns(unknowns, dir=u'.'):
    _save_as_module(os.path.join(dir, MODULE_UNKNOWNS), unknowns)


def _save(file, data, compresslevel):
    if not data:
        return
    with gzip.open(file, 'wb', compresslevel) as f:
        f.write(data)
        f.flush()


def _load(file):
    if not os.path.exists(file):
        return None
    with gzip.open(file, 'rb') as f:
        data = f.read()
        return data


def _save_as_module(file, data):
    if not data:
        return
    with open(file, 'w') as f:
        f.write(u'DATA=')
        if PY3:
            f.write(str(data))
        else:
            f.write(unicode(data))
        f.flush()


class Dictionary(object):
    u"""
    Base dictionary class
    """
    def __init__(self, compiledFST, entries, connections):
        self.compiledFST = compiledFST
        self.matcher = Matcher(compiledFST)
        self.entries = entries
        self.connections = connections

    def lookup(self, s):
        (matched, outputs) = self.matcher.run(s.encode('utf8'))
        if not matched:
            return []
        try:
            return [self.entries[unpack('I', e)[0]] for e in outputs]
        except Exception as e:
            logging.error('Cannot load dictionary data. The dictionary may be corrupted?')
            logging.error('input=%s' % s)
            logging.error('outputs=%s' % str(outputs) if PY3 else unicode(outputs))
            traceback.format_exc()
            sys.exit(1)

    def get_trans_cost(self, id1, id2):
        return self.connections[id1][id2]
