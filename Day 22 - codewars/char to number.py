# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is resultrect the errors in the digitised text. You only have to handle the following mistakes:

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(s):
#     return s.replace("5", "S").replace("1", "I").replace("0", "O")

    result=""
    
    for i in s:
        if i == "1":
            result += "I"
        elif i== "5":
            result += "S"
        elif i== "0":
            result += "O"
        else:
            result += i
    return result

print(correct("51NGAP0RE"))