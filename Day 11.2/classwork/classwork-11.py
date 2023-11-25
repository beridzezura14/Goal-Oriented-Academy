# # ფუნქციები:

import random

member_list = ["dato", "giga", "zura", "nika", "mio"]
cars_list = ["mercedes", "bmw", "toyota", "lexus", "porsche"]


for i in range(len(member_list)):

    name = random.choice(member_list)
    car = random.choice(cars_list)
    member_list.remove(name)
    cars_list.remove(car)

    def hello(name, car):
        print("hello " + name)
        print(name + " your car is:  " + car)

    hello(name, car)

# ფუნქციების სასუალებით ჩვენ შეგვიძლია თავიდან ავირიდოთ ხშირად გამეორეადი კოდები





# print("Credit:", 98)

# print(55 * 3) #math
# print(5 > 7) #comparison
# print(True and False) #logical
# print("motor" + "bike") #concatenation

# print("robot".find("A"))

# word = 'vehicle'
# print(word.find('r'))

# word = 'vehicle'
# print(word.find())





# text = input()

# upper = text.upper()                # ყველა ასოს ადიდებს
# lower = text.lower()                # ყველა სასოს აპატარავებს
# capitalize = text.capitalize()      # მარტო პირველ ასოს ადიდებს
# #display on the screen

# print(upper)
# print(lower)
# print(capitalize)


# print(-42 * 1)
# print(42 * -1)

# # # # # def make_negative(number):
# # # # #     num = number * (-1)
        
# # # # #     return num

# def make_negative(number):
#     return -abs(number)

# print (make_negative(-683))

# num_list = [5, -1, 2]
# def remove_negs(num_list): 
#     for item in num_list: 
#         if item < 0: 
#            num_list.remove(item) 

#     return num_list

# print(remove_negs(num_list))
# print(sum(remove_negs(num_list)))

# word = "hello"
# word = word[1:]
# word = word[:-1]
# print(word)


# t = 'This is a test!'
# print (t [1:-1])

# numbers = [1, 2, 3, 4, 5]

# def square_sum(numbers):
#     #your code here
#     square = [i ** 2 for i in numbers]
#     return square

# print(sum(square_sum(numbers)))
# num = 6
# def summation(num):
#     return num * (num + 1) // 2

# print(summation(num))



# def greet():
#     '''
# '　　＊'　　'　★'　　＊'　　'　 ￼
# ＊　.　 * .'　＊＊　　'＊　　　*
# ＊　　.　'　　+:..:+ 　　'　 ' 　＊
# .　　　＊　　☆☆☆　＊　　　.
# 　　*　　'　+:...+....:+　　＊
# '　　　　'　☆☆☆☆☆　　　＊　'　　
# 　＊　* '　+:...:+＠+:...:+ 　　　'　　*
# ＊　.　　.☆☆☆☆☆☆☆ ＊　'　*　.
# 　　.　　+:..:+&+:...:+:...:+
# 　*　.　☆☆☆☆☆☆☆☆☆　＊　'　　　*
# 　.　　+:...:+♡+:...:+§+:..:+
# .　*　☆☆☆☆☆☆☆☆☆☆☆　　'　*
# 　　.+:..:+♡+:..:+@+:..:+♡+:..:+
# 　.　　　　　.　▨ 　 '　' ＊　　　　　*
# 　　　.　*　　　　　　.　　　.　　'''
#     return 'hello world!'
# ------------------------------------
# number = 4
# def solution(number):
#    my_number = 0

#    if number % 2 == 0:
#       my_number += number

# print(solution(number))




