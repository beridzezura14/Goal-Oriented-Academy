# მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,და 
# შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა რომელ 
# სახელში არის მეტი,და დაპრინტეთ მიღებული შედეგი

# შევიტანთ სახელებს
name_1 = input("enter name-1: ")
name_2 = input("enter name-2: ")

x_name_1 = 0
x_name_2 = 0
# დავთვლით a-ს რაოდენობებს
for i in name_1:
    if i == "a":
        x_name_1 +=1
for i in name_2:
    if i == "a":
        x_name_2 +=1
# print(x_name_1)
# print(x_name_2)

# შევადარებთ და გამოვიტანთ შედეგს
if x_name_1 > x_name_2:
    print("'a' aris meti name-1-shi, raodenoba Seadgens: " + str(x_name_1) + "s")
    print("name-1 metia name-2-ze")
elif x_name_1 == x_name_2:
    print("'a' aris toli orive saxelshi " + str(x_name_1) + " = " + str(x_name_1))
else:
    print("'a' aris meti name-2-shi, raodenoba Seadgens: " + str(x_name_2) + "s")
    print("name-2 metia  name-1-ze")


