def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    knapsack = []

    for value, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
            knapsack.append((value, weight))
        else:
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((fraction * value, capacity))
            break

    return knapsack, total_value

# Example usage:
items = [(60, 10), (100, 20), (120, 30)]
knapsack, max_value = fractional_knapsack(items, 50)

print("Items in the Knapsack:")
for value, weight in knapsack:
    print(f"Value: {value}, Weight: {weight}")

print("Total Value in the Knapsack:", max_value)

# We sort the list of items by their value-to-weight ratio in 
# descending order, as the greedy approach aims to select items 
# with the highest value-to-weight ratio first.

# We initialize variables to keep track of the total value in the
# knapsack and the list of items placed in the knapsack.

# We iterate through the sorted items, and for each item, we check
# if it can be fully placed in the knapsack. If its weight is less
# than or equal to the remaining capacity, we add it to the knapsack
# and update the total value and remaining capacity. If it can only
# be placed partially, we add a fraction of the item to the knapsack 
# and break the loop.

# Finally, we return the list of items in the knapsack and the maximum 
# total value.

# This program will output the items placed in the knapsack and the
# maximum total value that can be achieved using a greedy approach
# for the Fractional Knapsack problem.

# # Theory:
# Fractional Knapsack Problem:

# The fractional knapsack problem is a variation of the knapsack problem. 
# In this problem, you are given a set of items, each with a weight and a 
# value. The goal is to determine the most valuable combination of items 
# to include in a knapsack with a limited weight capacity. Unlike the 0/1 
# knapsack problem, where you must either take an item in full or leave it,
# in the fractional knapsack problem, you can take a fraction of an item. 
# The objective is to maximize the total value of the items included while 
# staying within the weight capacity of the knapsack.

# Time and Space Complexity:

# - Time Complexity: The time complexity of the code is dominated by the 
# sorting step, which takes O(n log n) time, where 'n' is the number of 
# items. The loop that follows iterates through the sorted items once, 
# making it O(n) in terms of time complexity. So, the overall time 
# complexity is O(n log n) due to the sorting.

# - Space Complexity: The space complexity is primarily determined by 
# the space used to store the `knapsack`, which can have at most 'n' 
# items, so the space complexity is O(n).

# The code efficiently solves the fractional knapsack problem and returns 
# the optimal combination of items to maximize the total value within the weight 
# capacity of the knapsack.