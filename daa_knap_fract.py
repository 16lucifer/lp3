def fractional_knapsack(weights, values, capacity):
    items = sorted(
        [(v / w, w, v) for w, v in zip(weights, values)],
        reverse=True,
        key=lambda x: x[0],
    )
    total_value = 0.0
    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break
    return total_value


n = int(input("Enter number of items: "))
weights, values = [], []
for i in range(n):
    weights.append(float(input(f"Weight of item {i+1}: ")))
    values.append(float(input(f"Value of item {i+1}: ")))
capacity = float(input("Enter knapsack capacity: "))

print(f"Maximum value: {fractional_knapsack(weights, values, capacity)}")
