# problem statement


# Find percentage increased
# Write a function to calculate the percentage increase from the original value to the new value.

# Assume original is less than or equal to new.

# Examples

# >>> percentage_increased(50, 75)
# 50.0
# >>> percentage_increased(80, 100)
# 25.0

def percentage_increased(original, new):
    difference_between_them = (new - original)
    partincreased = (difference_between_them)/original 
    percentageincreased = (partincreased * 100)
    return (percentageincreased)


print (percentage_increased(50, 75))