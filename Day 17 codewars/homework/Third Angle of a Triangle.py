# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

def other_angle(a, b):
    return 180 - (a + b)   # The sum of the angles in a triangle is 180 
                           # if  we want to define 3rd angles 180 minuse sum of "a" and "b"

print(other_angle(10, 20))