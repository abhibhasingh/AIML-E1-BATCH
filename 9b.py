joint_prob = {}
n = int(input("Enter number of entries in joint distribution: "))
for _ in range(n):
    x = input("Enter value for X: ")
    y = input("Enter value for Y: ")
    p = float(input("Enter joint probability P(X,Y): "))
    joint_prob[(x, y)] = p

def marginal_x(joint):
    marginal = {}
    for (x, y), prob in joint.items():
        marginal[x] = marginal.get(x, 0) + prob
    return marginal

def marginal_y(joint):
    marginal = {}
    for (x, y), prob in joint.items():
        marginal[y] = marginal.get(y, 0) + prob
    return marginal

print("\nMarginal P(X):", marginal_x(joint_prob))
print("Marginal P(Y):", marginal_y(joint_prob))
