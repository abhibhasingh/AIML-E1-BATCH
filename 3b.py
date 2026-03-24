class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def depth_limited_search(node, goal, limit, current_depth=0, visited_order=None):
    if node is None:
        return False

    visited_order.append(node.value)

    if node.value == goal:
        return True

    if current_depth == limit:
        return False

    for child in node.children:
        if depth_limited_search(child, goal, limit, current_depth + 1, visited_order):
            return True

    return False


def iterative_deepening_dfs(root, goal, max_depth):
    for depth in range(max_depth + 1):
        visited_order = []
        print(f"\nIteration with depth limit = {depth}:")

        found = depth_limited_search(root, goal, depth, 0, visited_order)

        print("Visited order:", " ".join(visited_order))

        if found:
            print(f"Goal node '{goal}' found at depth {depth}")
            return

    print(f"\nGoal node '{goal}' not found within depth limit.")

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

goal = input("Enter goal node: ").strip()

max_depth = int(input("Enter maximum depth limit: "))

iterative_deepening_dfs(root, goal, max_depth)