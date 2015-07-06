# -*- coding: utf-8 -*-

import os
import sys
from xxx.lexer import lexer
from xxx.parser import parser

def main():
    from rjanome.lattice import NodeType
    from rjanome.lattice import BaseNode
    from rjanome.lattice import Node
    from rjanome.lattice import BOS
    from rjanome.lattice import EOS
    from rjanome.lattice import Lattice
    _1 = NodeType()
    _2 = BaseNode()
    _3 = Node((1,2,3,4,5,6,7,8,9,10))
    _4 = BOS()
    _5 = EOS(1)
    from rjanome.dic import PY3
    from rjanome.dic import Dictionary
    _d1 = Dictionary([], 1, [[1],[1,2]])  #TODO: xxx
    _d1_1 = Lattice(1, _d1)
    #print(hasattr(_3, 'surface'))
    #_d1_1.add(_3)

def eval(program_contents):
    r = main()
    print(parser.parse(lexer.lex(program_contents)).eval())

def run(fp):
    program_contents = ""
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        program_contents += read
    os.close(fp)
    eval(program_contents)

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print "You must supply a filename"
        return 1
    run(os.open(filename, os.O_RDONLY, 0777))
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
