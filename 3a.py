class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def depth_limited_search(node, limit, current_depth=0):
    if node is None:
        return

    print(node.value, end=" ")

    if current_depth == limit:
        return

    for child in node.children:
        depth_limited_search(child, limit, current_depth + 1)


nodes = {}

n = int(input("Enter number of nodes: "))

print("Enter node values:")
for _ in range(n):
    val = input().strip()
    nodes[val] = TreeNode(val)

e = int(input("Enter number of edges: "))

print("Enter edges (parent child):")
for _ in range(e):
    parent, child = input().split()
    nodes[parent].add_child(nodes[child])

root_val = input("Enter root node: ").strip()
root = nodes[root_val]

limit = int(input("Enter depth limit: "))

print("\nDLS Traversal:")
depth_limited_search(root, limit)