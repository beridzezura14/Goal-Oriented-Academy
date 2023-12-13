list_of_numbers = []

def add_extra(list_of_numbers):

    # return len(list_of_numbers) + 1

    # result = []

    # if list_of_numbers == []:
    #     result.append(1)

    # if len(list_of_numbers) > 0:
    #     result.append(len(list_of_numbers) + 1)

    # if list_of_numbers == []:
    #     result = 1

    # if len(list_of_numbers) > 0:
    #     result  = len(list_of_numbers) + 1
        
    # return result
    return list_of_numbers + [1]

print(add_extra(list_of_numbers))