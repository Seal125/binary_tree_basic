class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    values = []

    def add(node):
        if node:
            add(node.left)
            list.append(node.value)
            add(node.right)
    add(root)
    return values           

def is_unival_tree(tree):    
    value = tree.value
    is_unival= True

    def add(node):
        if node:
            add(node.left)
            if node.value != value:
                is_unival = False
                return is_unival
            add(node.right)
  