def to_alternating_case(string):
    result = ""
    for i in string:
        if i.isupper():   #The Python isupper() function will return a True or False value
            result += i.lower()
        else:
            result += i.upper()

    return result


    # return string.swapcase() short version
        
print(to_alternating_case("hELLO WOrLD"))
        
        