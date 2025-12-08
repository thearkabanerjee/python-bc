# problem 1

# Format Elements in tuple as "second, first"
# Given a tuple of length two create a string in the format of "second, first" where first and second are the first and second elements in the tuple.

# The elements can be of any data type.
# Change in eligibility criteria to write oppe2 exam: A5>=40/100 AND A6>=40/100 AND A7>=40/100 AND A8>=40/100. and becoming eligible to give the end term exam.

# Example

# >>> format_as_second_comma_first(('hello', 'python'))
# 'python, hello'
# >>> format_as_second_comma_first((1, 2))
# '2, 1'


def format_as_second_comma_first(t:tuple)-> str:
    listt = list(t)
    namey = (f'{listt[1]}, {listt[0]}')
    return (namey)
    # return (t(1),t(0))
    

testcases = format_as_second_comma_first(('hello', 'python'))
print (testcases)