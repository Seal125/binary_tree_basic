from exercises import Node, inorder, is_unival_tree
from typing import List

def test_inorder():
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.right.left = Node(4)
    t.right.right = Node(5)