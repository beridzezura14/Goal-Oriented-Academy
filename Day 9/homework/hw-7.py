# შემოიტანეთ სამი რიცხვი და დაპრინტეთ გამოვა თუ არა ამ 
# რიცხვების საშუალებით სამკუთხედი, თუ გამოვა გამოთვალეთ პერიმეტრი და დაპრინტეთ 
# "ამ სამკუტხედის პერიმეტრია: XX" თუ არ გამოდის მაშინ 
# დაპრინტეთ „მსგავსი სამკუთხედი არ არსებობს“

num1 = int(input("shemoitaneT cifri: "))
num2 = int(input("shemoitaneT cifri: "))
num3 = int(input("shemoitaneT cifri: "))

if ((num1 + num2) >= num3) and ((num2 + num3) >= num1) and ((num3 + num1) >= num2):
    print("sworia")
    perimeter = num1 + num2 + num3
    print("samkutxedis perimetria: " + str(perimeter) )
else:
    print("msgavsi samkuTxedi ar arsebobs")


