# Complete the function so that it finds the average 
# of the three scores passed to it and returns the letter 
# value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90   	'B'
# 70 <= score < 80  	'C'
# 60 <= score < 70``	'D'
# 0 <= score < 60	    'F'


def get_grade(s1, s2, s3):              # we create a function
    sum = (s1 + s2 + s3) / 3            # We created a variable and count avarage to this numbers            
    if sum >= 90:                       # after we use "if" statement to understend that avarage equals: A B C D or F
        return "A"                      # "A"
    if sum >= 80:                       # 80 and more
        return "B"                      # "B"
    if sum >= 70:                       # 70 and more                   
        return "C"                      # "C"            
    if sum >= 60:                       # 60 and more
        return "D"                      # "D"           
    return "F"                          # less then 60 automatic equals "F"  

print(get_grade(95, 100, 97))