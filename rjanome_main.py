from rjanome.lattice import NodeType
from rjanome.lattice import BaseNode
from rjanome.lattice import Node
from rjanome.lattice import BOS
from rjanome.lattice import EOS
from rjanome.lattice import Lattice

from rjanome.dic import PY3
from rjanome.dic import Dictionary


def main():
    _1 = NodeType()
    _2 = BaseNode()
    _3 = Node(("xxx",1,1,4,5,6,7,8,9,10))
    _4 = BOS()
    _5 = EOS(1)
    _d1 = Dictionary([], 1, [[1, 2],[1]])  #TODO: xxx
    _d1_1 = Lattice(2, _d1)
    _d1_1.add(_3)
