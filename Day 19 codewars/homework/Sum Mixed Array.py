# def sum_mix(arr):
#     x = int(arr)
#     result = sum(x)
#     return result



arr = ["3", "4", 5, 4]

def sum_mix(arr):
    # result = list(map(int, arr))
    # return sum(result)

    return ([int(x) for x in arr])    # string element convert to integer and summation
                                      # also we can convert integer to string 
print(sum_mix(arr))

