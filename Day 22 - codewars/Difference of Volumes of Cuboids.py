# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

# Your function will be tested with pre-made examples as well as random ones.

# If you can, try writing it in one line of code.



import math                                # import math library
def find_difference(a, b):
    result = math.prod(a) - math.prod(b)   # to multiply all values in the list using math.prod
    if result < 0:
        return result * -1   # acording to exemif number is negative become positive
    return result

# import math 

# def find_difference(a, b):
#     return abs(math.prod(a) - math.prod(b))  # abs the number is always positive

print(find_difference([3, 2, 5], [1, 4, 4]))


