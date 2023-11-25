
# 1) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ასაკი და დაპრინტეთ გრძელ წინადადებაში ყველა ეს მონაცემი.
# 2) მომხმარებელს შეეკითხეთ ასაკი, და დაუპრინტეთ 25 წელში რამდენი წლის  იქნება

# first version

print ("input your name")
name = input()
print("name is: " + name)

print ("input your lastname")
lastname = input()
print("lastname is: " + lastname)

print ("input your age")
age = int(input())
print("your age is: " + str(age))

print("Your name is " + name + ", your lastname is " + lastname +  " and age is " + str(age))

age_plus = age + 25

print("after 25 years you will be: " + str(age_plus))
