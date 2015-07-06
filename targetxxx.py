# -*- coding: utf-8 -*-

import os
import sys
from xxx.lexer import lexer
from xxx.parser import parser

def eval(program_contents):
    from rjanome_main import main
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
