class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def display_tree(node, level=0):
    print("  " * level + node.data)

    for child in node.children:
        display_tree(child, level + 1)