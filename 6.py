import math

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp():
    # 1. Take User Input
    try:
        n = int(input("Enter the number of cities: "))
        cities = []
        for i in range(n):
            coords = input(f"Enter x,y coordinates for City {i} (e.g., 10,20): ")
            x, y = map(float, coords.split(','))
            cities.append((x, y))
    except ValueError:
        print("Invalid input. Please enter numbers in the format: x,y")
        return

    # 2. Nearest Neighbor Heuristic
    unvisited = list(range(1, n))
    tour = [0]
    total_dist = 0
    current = 0

    while unvisited:
        # Find closest unvisited city
        next_city = min(unvisited, key=lambda x: get_distance(cities[current], cities[x]))
        
        # Update path and distance
        total_dist += get_distance(cities[current], cities[next_city])
        current = next_city
        tour.append(current)
        unvisited.remove(current)

    # 3. Return to Start
    total_dist += get_distance(cities[current], cities[tour[0]])
    tour.append(tour[0])

    # 4. Output Results
    print("\n--- Results ---")
    print(f"Optimal Path (Heuristic): {' -> '.join(map(str, tour))}")
    print(f"Total Travel Distance: {total_dist:.2f}")

if __name__ == "__main__":
    solve_tsp()