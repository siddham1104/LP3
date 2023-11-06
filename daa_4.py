def solve_knapsack():
    val = [50, 100, 150, 200]  # Value array
    wt = [8, 16, 32, 40]  # Weight array
    W = 64
    n = len(val) - 1

    def knapsack(W, n):
        # Base case
        if n < 0 or W <= 0:
            return 0, []

        # Higher weight than available
        if wt[n] > W:
            return knapsack(W, n - 1)

        # Calculate value if we include the current item
        include_value, include_weights = knapsack(W - wt[n], n - 1)
        include_value += val[n]

        # Calculate value if we exclude the current item
        exclude_value, exclude_weights = knapsack(W, n - 1)

        # Determine the choice that maximizes the value
        if include_value > exclude_value:
            # Include the current item
            include_weights.append(wt[n])
            return include_value, include_weights
        else:
            # Exclude the current item
            return exclude_value, exclude_weights

    max_value, selected_weights = knapsack(W, n)
    print("Maximum Value:", max_value)
    print("Selected Weights:", selected_weights)

if __name__ == "__main__":
    solve_knapsack()


# Explanation of the Code:

# 1. `solve_knapsack` function:
#    - This function is the entry point for solving the 0-1 knapsack problem.
#    - It initializes two arrays: `val`, which contains the values of items, 
#      and `wt`, which contains the weights of items.
#    - It also defines the knapsack's weight capacity `W`.

# 2. Nested `knapsack` function:
#    - Inside the `solve_knapsack` function, there's a nested `knapsack` 
#      function that is defined to implement the recursive solution to the 0-1 knapsack problem.
#    - It takes two parameters: `W` (remaining weight capacity) and `n` (the number of items checked).

# 3. Base case:
#    - The `knapsack` function starts with a base case: if `n` is less than 0 or `W` is less than 
#      or equal to 0, it returns 0. This means that if no more items are left to consider or if 
#      there's no capacity left in the knapsack, the function returns 0.

# 4. Recursive cases:
#    - If the current item's weight `wt[n]` is greater than the remaining capacity `W`, it means
#      that this item cannot be included. In this case, it calls the `knapsack` function with 
#      the same weight capacity `W` and the previous item `n-1`.
#    - If the item's weight is less than or equal to the remaining capacity, it considers two options:
#      - Including the current item: It calculates the total value by adding the value of the 
#      current item (`val[n]`) to the result of the `knapsack` function called with reduced
#      capacity (`W-wt[n]`) and the previous item (`n-1`).
#      - Not including the current item: It calculates the total value by calling the `knapsack`
#       function with the same capacity `W` and the previous item `n-1`.
#    - It returns the maximum value of the two options (including or not including the current item).

# 5. Printing the result:
#    - The `solve_knapsack` function then prints the result by calling the `knapsack` function with 
#      the given weight capacity `W` and the index of the last item `n`.

# 0-1 Knapsack Problem:

# The 0-1 knapsack problem is a classic optimization problem. Given a set of items, each with a weight 
#  and a value, the goal is to determine the most valuable combination of items to include in a knapsack
#  with a limited weight capacity. In the 0-1 knapsack problem, each item can either be included (1) or 
#  not included (0), and you cannot take a fraction of an item. The objective is to maximize the total value 
#  of the items in the knapsack while staying within the weight capacity.

# Time and Space Complexity:

# - Time Complexity: The code uses a recursive approach to solve the problem. It explores all possible 
# combinations of items (either including or not including each item) using recursion. The time complexity
#  of this code is exponential, specifically O(2^n), where 'n' is the number of items. This is because the
#  function is called recursively for each item, and there are 2^n possible combinations to consider.

# - Space Complexity: The space complexity is determined by the depth of the call stack during the 
# recursive calls. In the worst case, the call stack can grow as deep as 'n,' resulting in a space 
# complexity of O(n).