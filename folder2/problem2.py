# problem 2 

# Check if ten digit even number
# Write a function to check if a number is a ten-digit even number.
# Also account for negative numbers discarding the sign.

# Examples

# >>> is_ten_digit_even(8769473839)
# False
# >>> is_ten_digit_even(928948)
# False
# >>> is_ten_digit_even(9289479278)
# True
# >>> is_ten_digit_even(-9289479278)
# True

def is_ten_digit_even(n):
    n = abs(n)

    if ((len(str(n)) == 10) and (n%2 == 0)) :
        return True
    else:
        return False

test_Cases = is_ten_digit_even(8769473839)

print (test_Cases)

