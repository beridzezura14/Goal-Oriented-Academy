
def is_palindrome(s):
    # x = s.lower()

    # even_first_part = x[:len(x)//2]
    # even_second_part = x[len(x)//2:]

    # first_part = x[:len(x)//2]
    # second_part = x[len(x)//2:]
    # third_part = second_part[::-1]
    # finally_part = third_part[:len(third_part)-1]

    # if len(s) < 2:
    #     return True
    # elif len(s) < 4 and x[0] == x[-1]:
    #     return True
    # elif len(x) % 2 == 0 and even_first_part == even_second_part[::-1]:
    #     return True
    # elif len(x) % 2 == 1 and first_part == finally_part:
    #     return True    
    # return False
    s = s.lower()
    if s == s[::-1]:
        return True
    return False    
print(is_palindrome("abba"))

# print(is_palindrome("GGGHHhhhhhh"))


# ----------------------------------------------------------------------





# x = "abbba"

# print(x[::-1])
# first_part = x[:len(x)//2]
# second_part = x[len(x)//2:]
# third_part = second_part[::-1]
# finally_part = third_part[:len(third_part)-1]
# print(first_part == finally_part)
# print(first_part == second_part[::-1])


