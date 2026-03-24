import heapq
1
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth 

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for move, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]

                # Swap blank (0)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

                successors.append(Puzzle(new_state, self, move, self.depth + 1))

        return successors

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def astar(initial_state):
    start = Puzzle(initial_state)

    pq = []
    counter = 0

    heapq.heappush(pq, (0, counter, start))
    visited = set()

    while pq:
        _, _, current = heapq.heappop(pq)

        state_tuple = tuple(tuple(row) for row in current.state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current.is_goal():
            return current

        for child in current.generate_successors():
            child_tuple = tuple(tuple(row) for row in child.state)

            if child_tuple not in visited:
                g = child.depth
                h = manhattan_distance(child.state)
                f = g + h

                counter += 1
                heapq.heappush(pq, (f, counter, child))

    return None

def print_solution(solution):
    path = []
    current = solution

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("\nSolution found in", len(path) - 1, "moves:\n")

    for step in path:
        print("Move:", step.move)
        step.display()

print("8-Puzzle Solver using A* Search\n")

print("Enter the initial state (3x3 grid)")
print("Use space-separated values (0 represents blank)\n")

initial_state = []

for i in range(3):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    initial_state.append(row)

print("\nInitial State:")
for row in initial_state:
    print(row)

solution = astar(initial_state)

if solution:
    print_solution(solution)
else:
    print("No solution found.")