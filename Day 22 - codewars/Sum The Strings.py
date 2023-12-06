# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"
# Notes:

# If either input is an empty string, consider it as zero.

# Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    if a == a and b == "":
        return a
    if a == "" and b == b:
        return b    
    
    a = int(a)
    b = int(b)
    return str(a + b)

print(sum_str("4","5"))