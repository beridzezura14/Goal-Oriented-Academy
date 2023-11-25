
# sequensing - კომპი უშვებს კოდს ზევიდან ქვევით ერთმანეთის მიყოლებით

# iteration - რაღაცის გამეორება ე.წ. loop

# selection - როცა გატყობინებს რაღაც ინფორმციას მაგ: გაზრდილი გულის ცემა (არჩევა)

# algorithms  ინსტრუქცია რომელსაც მივყვებით  ---->  flowcharts  გვეხმარება ვიზუალიზაციაში


#  ------ for loop -------------

# Define the number of iterations
for i in range(100):
 #Statement that gets repeated
 print("Hello")

# i - საიტერაციო(iteration) ცვლადი - განმეორებითი
# range - დიაპაზონი

# ------ class exercise  1 wey ----------------

name = input("name: ")
age = int(input("age: "))
year = int(input("year: "))

for i in range (10):
    print(name + " Sen iqnebi " + str(age + i) + " wlis " + str(year + i) + " wels")


# ---------------------------

# Loop using i as internal variable
for i in range(3):
  print(i)

print("--")   #This is just a separator

#Loop using "something" as internal variable
for something in range(3):
  print(something)

# -------------- while loop ---------

seats = 10 # initial number of seats
while seats > 0: # seat available?
  print("Sell ticket") # ticket sold
  print("darchenilia " + str(seats))
  seats = seats - 1 # number of seats updated




