products = ["juice", "chocolate", "water"]
user_choice = 1
print(products[user_choice])  # print chocolate


for i in range(40, 60):
    print(i)   # დაიპრინტება 40 - 59

for i in range(40, 60, 5):
    print(i)   # დაიპრინტება 40 - 59მდე ყველა მეხუთე ციფრი


for i in "zura":
    print(i)  #დაიპრინტება zura ვერტიკალუტად

    # z
    # u
    # r
    # a

products = ["juice", "chocolate", "water"]
products.append("milk") # დაემატება milk
products.insert(2, "cocoa") # დაემატება 2-ის შემდეგ cocoa

print(products) # დდაიბეჭდდება ['juice', 'chocolate', 'cocoa', 'water', 'milk']
print(len(products)) # დაიბეჭდება რაოდენობა



my_str = "nika 11 keshelava"
print(my_str[5] + my_str[6] + "4") # print - 114



num1 = int(input("enter num1: "))  #13
num2 = int(input("enter num2: "))  #20
num3 = int(input("enter num3: "))  #7

my_sum = 0

if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1:
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3

print("number is {}".format(my_sum)) # მიღებული ციფრი ანუ 20 ჩაჯდება ფიგურულ ფრჩხილში

print("number is " + str(my_sum)) # ასეც იმუსავებს