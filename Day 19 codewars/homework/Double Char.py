# Given a string, you have to return a string in which 
# each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!


s = "String"

def double_char(s):
    char = ""
    for i in s:
        char += i + i

    return char

print(double_char(s))   # print ssttrriinngg
        