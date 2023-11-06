def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    if n <= 1:
        return n

    first = 0
    second = 1

    for _ in range(n - 2):
        third = first + second
        first = second
        second = third

    return second  # Return the nth Fibonacci number

if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(recursive_fibonacci(i))

    nth_fib = non_recursive_fibonacci(n)
    print(f"The {n}th Fibonacci number is {nth_fib}")


# Explaination:

# 1. `recursive_fibonacci` function:
#    - This function calculates the nth Fibonacci number using a recursive approach.
#    - It starts with the base case: if `n` is 0 or 1, it returns `n` 
#      because the 0th and 1st Fibonacci numbers are 0 and 1, respectively.
#    - For `n` greater than 1, it recursively calls itself with `n-1` 
#      and `n-2` and adds their results to calculate the nth Fibonacci number.
#    - The function prints the Fibonacci numbers for each value from 0 
#      to 9 (i.e., the first 10 Fibonacci numbers).

# 2. `non_recursive_fibonacci` function:
#    - This function calculates the nth Fibonacci number using a non-recursive (iterative) approach.
#    - It also handles the base case: if `n` is 0 or 1, it directly returns `n`.
#    - For `n` greater than 1, it uses a loop to iteratively calculate the 
#      Fibonacci numbers. It starts with `first` and `second` set to 0 and 1, respectively.
#    - Inside the loop, it calculates the next Fibonacci number (`third`) by 
#      adding `first` and `second`, updates the values of `first` and `second`, 
#      and continues the loop until it reaches the `n`th Fibonacci number.
#    - The function returns the nth Fibonacci number.

# In the main part of the code:
# - It sets `n` to 10, which means it will calculate and print the first 10 Fibonacci numbers.
# - It first uses the `recursive_fibonacci` function to print the Fibonacci 
#   numbers from 0 to 9.
# - Then, it uses the `non_recursive_fibonacci` function to calculate and store 
#   the 10th Fibonacci number and prints it along with a message.

# Analysis:
# Recursive:
# Time Complexity: The time complexity of this recursive approach is exponential, 
# specifically O(2^n). This is because the function makes two recursive calls for 
# each value of n, and the number of function calls grows exponentially with n. It 
# recalculates the same Fibonacci numbers multiple times, leading to inefficient 
# computations for larger values of n.

# Space Complexity: The space complexity of the recursive approach is determined by 
# the depth of the call stack. In the worst case, the call stack can grow as deep as n, 
# resulting in a space complexity of O(n).

# Non-recursive:
# Time Complexity: The time complexity of the non-recursive (iterative) approach is O(n). 
# It iterates through a loop n - 2 times, where each iteration involves basic arithmetic 
# operations. This approach is much more efficient than the recursive approach.

# Space Complexity: The space complexity of the non-recursive approach is O(1) because it 
# uses a constant amount of additional space to store the variables (first, second, third) 
# and does not rely on a recursive call stack.

# In summary, the non-recursive (iterative) approach is more efficient in terms of both 
# time and space complexity for calculating Fibonacci numbers compared to the recursive 
# approach, especially for larger values of n. The recursive approach has exponential 
# time complexity and linear space complexity, making it less suitable for large Fibonacci 
# numbers.