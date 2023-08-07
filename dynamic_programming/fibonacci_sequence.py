"""
Classic fibonacci sequence

Create a function that returns the nth value in the fibonacci sequence
"""

def nth_fibonacci_term(n = int):
    """
    takes in n which represents index integer, returns an integer corresponding with value
    """
    # initialize a list with first two terms to store the sequence
    fibonacci_list = [0, 1] 

    # first two cases
    if n == 0:
        return fibonacci_list[0]
    elif n == 1:
        return fibonacci_list[1]
    
    # without using recursion, calculate and store all values into the list
    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    
    # runs in O(n) time
    return fibonacci_list[-1]

print(nth_fibonacci_term(5))