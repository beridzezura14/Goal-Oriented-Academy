# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

s = "hello!!!!!!!!!!!!!world!!!!!!!!!!!!"

def remove_exclamation_marks(s):       # we create a function
    result = ""                        # we create a variable which is empty
    for i in s:                        # და დავატრიალეთ for ციკლი
        if i != "!":                   # if every value don't equal Exclamation Marks (ყოველ დატრიალებაზე თუ მნიშვნელობა არიქნება ტოლი ძახილის ნიშანის)  
            result += i                # add to "result"  (დაემატოს result ცვლადს)
    return result


print(remove_exclamation_marks(s))


# return s.replace('!', '')  this is short vesion with "replase"