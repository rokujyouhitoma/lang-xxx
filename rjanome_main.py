# -*- coding: utf-8 -*-
from rjanome.lattice import NodeType
from rjanome.lattice import BaseNode
from rjanome.lattice import Node
from rjanome.lattice import BOS
from rjanome.lattice import EOS
from rjanome.lattice import Lattice

from rjanome.dic import PY3
from rjanome.dic import Dictionary


def main():
#     _1 = NodeType()
#     _2 = BaseNode()
#     _3 = Node(("xxx",1,1,4,5,6,7,8,9,10))
#     _4 = BOS()
#     _5 = EOS(1)
#     _d1 = Dictionary([], 1, [[1, 2],[1]])  #TODO: xxx
#     _d1_1 = Lattice(2, _d1)
#     _d1_1.add(_3)

    from rjanome.dic import SystemDictionary
    from sysdic import entries, connections, chardef, unknowns
    SYS_DIC = SystemDictionary(entries.DATA, connections.DATA, chardef.DATA, unknowns.DATA)

    #from sysdic import SYS_DIC
    s = u'４日夜、満月が地球の影に完全に入る「皆既月食」が起きた。'
    lattice = Lattice(len(s), SYS_DIC)
    pos = 0
    while pos < len(s):
        entries = SYS_DIC.lookup(s[pos:])
        for e in entries:
            lattice.add(Node(e))
        pos += lattice.forward()
    lattice.end()
    #print(str(lattice))

    min_cost_path = lattice.backward()
    for node in min_cost_path:
        if isinstance(node, Node):
            print(node.surface + '\t' + node.part_of_speech)



if __name__ == '__main__':
    main()
