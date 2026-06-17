class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(prefix + connector + str(node.data))

    prefix += "    " if is_last else "│   "

    for i, child in enumerate(node.children):
        print_tree(child, prefix, i == len(node.children) - 1)