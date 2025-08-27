def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Factorial of n (n!) is the product of all positive integers from 1 to n.
    By definition: 0! = 1
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    
    # Base case 1: Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Base case 2: Check for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case 3: Factorial of 0 is 1 (termination condition)
    if n == 0:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    # The function calls itself with a smaller value (n-1)
    # This creates a chain of recursive calls until we reach the base case
    return n * factorial(n - 1)


# Example usage and demonstration
if __name__ == "__main__":
    # Test the factorial function with various inputs
    test_values = [0, 1, 5, 7, 10]
    
    print("Factorial Calculation Examples:")
    print("=" * 30)
    
    for num in test_values:
        result = factorial(num)
        print(f"{num}! = {result}")
    
    print("\n" + "=" * 30)
    print("ALGORITHM FLOW SUMMARY:")
    print("=" * 30)
    print("""
1. INPUT VALIDATION:
   - First checks if input is an integer
   - Then verifies it's non-negative
   - These are the first base cases that prevent invalid operations

2. TERMINATION CONDITION:
   - When n == 0, returns 1 (0! = 1 by definition)
   - This stops the recursion and starts the unwinding process

3. RECURSIVE PROCESS:
   - For n > 0: n! = n * (n-1)!
   - Each recursive call reduces the problem size by 1
   - Creates a call stack: factorial(5) → factorial(4) → factorial(3) → etc.

4. UNWINDING PHASE:
   - Once base case is reached (n=0), the calls start returning
   - Each function returns its result to the previous caller
   - The results are multiplied in reverse order of the calls

Example for factorial(3):
- factorial(3) calls factorial(2)
- factorial(2) calls factorial(1) 
- factorial(1) calls factorial(0)
- factorial(0) returns 1
- factorial(1) returns 1 * 1 = 1
- factorial(2) returns 2 * 1 = 2  
- factorial(3) returns 3 * 2 = 6

Time Complexity: O(n) - linear time
Space Complexity: O(n) - due to call stack (each recursive call adds to stack)
""")
