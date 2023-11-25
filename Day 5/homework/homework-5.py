# 1) მომხმარებელს კითხეთ თავისი და მამამისის ასაკი, 
# დაუპრინტეთ ყოველ წელს რამდენჯერ უფროსი იქნება მამამისი მასზე.

son_age = int(input("enter son age: "))
dad_age = int(input("enter dad age: "))
current_year = int(input("enter current year: "))
sum_age = dad_age - son_age

for i in range(10):
    print("mamachemi am wels " + str(current_year + i) + " iqneba " + str(sum_age) + "-it ufrosi chemze")

# 2) 0 იდან 30-ის ფარგლებში დაპრინტეთ ყველა ლუწი და კენტი რიცხვი, მიუწერეთ გვერდზე 
# კენტია თუ ლუწი

i = 1
while i < 30:
  print(i, "odd")
  print(i+1, "even")
  i += 2



