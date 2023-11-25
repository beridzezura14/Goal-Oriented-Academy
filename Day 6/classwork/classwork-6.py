
# 3-ის ჯერადი - დავალება

# Indentation error 
i = 0
while i < 30:
  print(i+3, "არის 3-ის ჯერადი") # there is Indentation error 
  i += 3


# i = 0
# while i < 30:
#   print(i+3, "არის 3-ის ჯერადი")  # there is correct version
#   i += 3



# age = 18
# if age >= 18:
#     print("regular price")
# else:
#     print("dicount")

  
# num_1 = 20
# num_2 = 10

# print(num_1 != num_2)

# is_student = False
# age = 16
# print(is_student and (age < 18))


# START if/else ------------------------

# is_student = True
# age = 32
# if age < 18 or is_student:    
#     print("discount")
# else:
#     print("regular price")
    

age = 75

if age < 18:
    print("junior dis")    # პირობიდან გამომდინაარე ეს ველი გამოტოვა
elif age >= 75:
    print("senior dis")   # პირობიდან გამომდინაარე ეს ველი შეასრულა
else:
    print("no dis")   # პირობიდან გამომდინაარე ეს ველი გამოტოვა
print("Proced to pay")


age = 16
is_student = True
if age < 18:
    if is_student:
      print("20%")
    else:
      print("10%")    
else:
    print("regular")  
print("Proced to pay")


