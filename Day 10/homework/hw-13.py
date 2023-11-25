# შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 
# 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !#*#%(*#)^#, 2 
# სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347

# მაგ: !n8391k*

import random

password = ""

letter = "hbvahvksdfhvbks"
number = "6928475692837"
symbol = "@#$%!?/^"

for i in range(2):
    password += random.choice(number)
    password += random.choice(symbol)

for i in range(4):
    password += random.choice(letter)

print(password)

