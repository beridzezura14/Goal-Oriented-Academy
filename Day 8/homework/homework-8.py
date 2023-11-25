# დავალება 1)
# შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი.


number = [45, 24, 87, 55, 62, 16, 115, 200]
# number_sum = number[0] + number[1] + number[2] + number[3] + number[4] + number[5]  long way
number_sum = sum(number)  # short way 

print(number_sum)

for num in number:
    if num % 2 == 0:
        print(num, " ეს არის ლუწი")
    else:
        print(num, " კენტი")

# ------------------------------

# დავალება 2)
# ბილეთი ღირს 25 ლარი, მაგრამ ბავშვებისთვის უფასოა, გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 

price_adult = 25
price_children = 0

adult = 18

people = int(input("people: "))   # 10
children = int(input("children: "))  # 3

adult_price = people * price_adult            # 10 * 25
children_price = children * price_children    # 3 * 0
sum = adult_price + children_price            # 250 + 0 

print("sul gadsaxadia", sum)                  # სულ საჭიროა 250

# ------------------------------

# დავალება 3)
# მომხმარებელს შემოატანინეთ სახელი,
# და დაპრინტეთ ეს სახელი იმდენჯერ, რამდენი ასოც არის სახელში.


#  1 გზა
name = input("enter your name: ")  # zura  ilo 
quantity = (name + " ") * len(name)
print(quantity)   # zura zura zura zura    ilo ilo ilo 

#  2 გზა
name_2 = input("enter your name: ")
len(name_2)
i = 0

while i < len(name_2):
    print(name_2)
    i += 1

# zura 
# zura 
# zura 
# zura

# ------------------------------

# დავალება 4)

# GOA ში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ.
# მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შემოიყვანა ხოლო თითო შემოყვანილ ადამიანზე დაერიცხოს 100ლ

# 1) რამდენი დაგერიცხება თუ შემოიყვან 10 ბავშვს?  15 ბავშცს?

# 2) რამდენი დაგერიცხება თუ შემოიყვან 100 ბავშვს გამოკლებული 37 დამატებული 13 გაყოფილი 10 და გამრავებული 264 ზე

user = int(input("how many people enter in GOA: ")) #10 #15
reward = 100
result = reward * user

#1
print("you recive " + str(result) + " gel")  

magic_number = 100 - 37 + 13 / 10 * 264

#2
print("you recive " + str(magic_number) + " gel")


# ------------------------------


# დავალება 5)
# HARDEST BOSS:
# დაპრინტეთ hello world (ოღონდ არა ასე print("hello world"))

#1
word = ["hello","goodbay","world", "land"]
print(word[0], word[2])

#2
# num = int(input("enter eny number: "))
num = 14

if num <= 1 or num >= 1:
    print("hello world")
else:
    print("nothing")

