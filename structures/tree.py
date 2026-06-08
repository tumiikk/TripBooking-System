class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    print("  " * level + str(node.data))

    for child in node.children:
        print_tree(child, level + 1)