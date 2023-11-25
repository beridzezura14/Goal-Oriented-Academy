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

