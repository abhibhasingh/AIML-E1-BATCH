def probability(favorable_outcomes, total_outcomes):
    if total_outcomes == 0:
        return "Total outcomes cannot be zero."
    
    prob = favorable_outcomes / total_outcomes
    return prob

favorable = int(input("Enter number of favorable outcomes: "))
total = int(input("Enter total number of outcomes: "))

result = probability(favorable, total)
print(f"P(A) = {result}")
