# binary - ორიბითი
# decimal - ათობითი

a = 3
b = "8"
print(a + b)   # you can't do math with strings, it will be TypeError

# when number is in quotation marks its string for exemple" 

a = "14"
print(type(a))  # ansver is "a string"

# type() - describe is it value string(integer) or not 

x = 9
y = 3

print(x / y) # ansver is - 3.0 (float)
print(x // y) # ansver is - 3 (integer)

birth_year = input()
print(type(birth_year)) # it define is it value integer or not

a = input()         # a string
b = int(input())    # a integer

a = 3
b = float(a)        # float change 3 > 3.0 
print(b) 

x = 5 
y = 2 

z = x/y # float (implicit conversion)   implicit - ავტომატური

print(z) # ansver 2.5


x = input()
y = input()      # string type
print(x+y)


# 1 way -----
x = int(input()) 
y = int(input())  # integer type
print(x+y)

# 2 way -----
x = input()
y = input()    # integer type
print(int(x) + int(y))


print(12/6)  # implicit data type conversion

# ----------------------

# true - falese

# boolean has two possible values - true and falese

print(3 > 15)   # falese

print(3 < 15)   # true

# binary - ორიბითი

# binary 0 - 1

# 0 - false
# 1 - true

print(type(5 < 9))
print(type(50 > 100))
print(type(True))
print(type(False))       # all of them is - class 'bool'

# comparison operation - შედარებითი ოპერაცია

# ----------------------  

# start  --->  input / output

# take several boolean  -  input
# produces only 1 Boolean  -  output

# True and True = True - Every other combination = False   pay attantion "and"
# True or False = True - True value if at least one of the inputs is True    pay attantion "or"

# True and True    = True 
# True and False   = False 
# False and True   = False        and
# False and False  = False

# True or True     = True 
# True or False    = True 
# False or True    = True         or
# False or False   = False

a = (3 > 2) or False  
print(a)  # true