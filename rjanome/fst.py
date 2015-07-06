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

from __future__ import division
from __future__ import print_function
import sys
import copy
from struct import pack, unpack
from collections import OrderedDict
import logging
import time
import threading

PY3 = sys.version_info[0] == 3

# bit flags to represent class of arcs
# refer to Apache Lucene FST's implementation
FLAG_FINAL_ARC = 1 << 0             # 1
FLAG_LAST_ARC = 1 << 1              # 2
FLAG_TARGET_NEXT = 1 << 2           # 4  TODO: not used. can be removed?
FLAG_STOP_NODE = 1 << 3             # 8  TODO: not used. can be removed?
FLAG_ARC_HAS_OUTPUT = 1 << 4        # 16
FLAG_ARC_HAS_FINAL_OUTPUT = 1 << 5  # 32

# all characters
CHARS = set()


class State(object):
    # TODO: xxx
    pass


def copy_state(src, id):
    state = State(id)
    state.final = src.final
    for c, t in src.trans_map.items():
        state.set_transition(c, copy.copy(t['state']))
        state.set_output(c, t['output'])
    state.final_output = copy.copy(src.final_output)
    return state


class FST(object):
    # TODO: xxx
    pass


# naive implementation for building fst
# http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.3698
def create_minimum_transducer(inputs):
    # TODO: xxx
    pass

def compileFST(fst):
    u"""
    convert FST to byte array representing arcs
    """
    # TODO: xxx
    pass


class Matcher(object):
    def __init__(self, dict_data, max_cache_size=5000, max_cached_word_len=15):
        if dict_data:
            self.data = dict_data
            self.data_len = len(dict_data)
            # bytes -> (position, final_outputs, outputs)
            self.cache = OrderedDict()
            self.max_cache_size = max_cache_size
            self.max_cached_word_len = max_cached_word_len
            self.lock = threading.Lock()

    def run(self, word, common_prefix_match=True):
        # TODO: xxx
        pass

    def next_arc(self, addr=0):
        # TODO: xxx
        pass
