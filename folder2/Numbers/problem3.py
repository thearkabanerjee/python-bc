# problem statement 3


# Arithmetic Operations tuple from two integers
# Given a tuple of two integers (a, b), return a tuple containing the sum, difference, product, and quotient (integer division) of the two numbers.
# Example:

# >>> arithmetic_operations((1, 2))
# (3, -1, 2, 0)



    
def arithmetic_operations(t:tuple) -> tuple:
    sum = t[0] +t[1]
    difference = t[0] - t[1]
    product = t[0] * t[1]
    quotient = t[0] // t[1]
    return (sum, difference,product, quotient )


testcases = arithmetic_operations((10, 5))
print (testcases)