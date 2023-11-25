# Given an array of integers.

# Return an array, where the first element is the count of 
# positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], 
# you should return [10, -65].Given an array of integers.


# def count_positives_sum_negatives(arr):
#     x = 0
#     z = 0
#     if not arr: return []
#     for i in arr:
#         if i > 0:
#            x += 1
#         if i < 0:
#             z += i        
#     return [x,z]

# arr = []

# def count_positives_sum_negatives(arr):
#     x = 0
#     z = []
#     y = sum(z)
#     if arr == []:
#         return []
#     for i in arr:
#         if i > 0:
#            x += 1
#         if i < 0:
#            z.append(i)
#            y = sum(z)         
#     return [x,y]
    

# print(count_positives_sum_negatives(arr))








# Given a non-empty array of integers, return the result of multiplying 
# the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# arr = [1, 2, 3, 4, 6]
# def grow(arr):
#     result = 1
#     for i in arr:
#          result = result * i
#     return result


# import math
# def grow(arr):
#     return math.prod(arr)


# print(grow(arr))


# arr = "46549845165165"

# result = ""

# for i in arr:
#     if i >= "5":
#         result += "1"
#     else:
#         result += "0"


# print(result)



# def smash(words):
#     return " ".join(words) # გაერთიანება 




# def check(seq, elem):  #  ლისთის შედარება ერთ ციფრზე ან სტრინგზე
#     if elem in seq:
#         return True    
#     return False

# def string_to_array(s):
#     if s == "":
#         return  ['']
#     return s.split()

# print(string_to_array(""))

# def string_to_array(s):    # short version
#     return s.split(' ')


# number = int(input("Enter the integer number: "))  
  
# revs_number = 0  
  
# while (number > 0):  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
  
# print("The reverse number is :",revs_number) 
# def reverse_seq(n):
#     result = []
#     for i in range (n, 0, -1):
#         result.append(i)
#     return result
# print(reverse_seq(5)) # result [5, 4, 3, 2, 1]


# versiebi:
# def reverseseq(n):
#     return range(n, 0, -1)

# def reverseseq(n):
#     return [x for x in range(n,0,-1)]


# ------------------------------------------------------------------------------------

# Is n divisible by x and y?

# Create a function that checks if a number n is divisible by two numbers x AND y. 
# All inputs are positive, non-zero numbers.

# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5



# def is_divisible(n,x,y):
#     if n % x == 0 and n % y == 0:
#         return True
#     return False


# ------------------------------------------------------------------------------------

# Create a function with two arguments that will return an 
# array of the first n multiples of x.

# Assume both the given number and the number of times to 
# count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]


# def count_by(x, n):
#     sum = x * n
#     result = []
#     for i in range (x, sum + 1, x):
#         result.append(i)
#     return result
    

# ------------------------------------------------------------------------------------

# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.

# Can you help her?

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
    
print(greet("Johnny"))


# ------------------------------------------------------------------------------------
# If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example, return a string with a murmur: 

# "1 sheep...2 sheep...3 sheep...". 

# Input will always be valid, i.e. no negative integers.

# def count_sheep(n):
#     # your code
#     result = []
#     finally_result = ""
    
#     for i in range(1,n+1,1):
#         result.append(str(i) + " sheep...")
        
#     for i in result:
#         finally_result += i
    
#     return finally_result

# print(count_sheep(5))



# # second and short version

# def count_sheep(n):
#     sheep = ""
#     for i in range(1, n + 1):
#         sheep += str(i) + " sheep..."
#     return sheep


# ------------------------------------------------------------------------------------

# Quarter of the year

# def quarter_of(month):
#     if month in range(1,4):
#         return 1
#     if month in range(4,7):
#         return 2
#     if month in range(7,10):
#         return 3
#     if month in range(10,13):
#         return 4   
# print (quarter_of(12))

# # def quarter_of(month):
# #     return (month + 2) // 3   




# return - შეინახავს მეხსიერებაში და როც გვინდა გამოვიძახებთ
# სიმრავლე არის რიცხვების სია