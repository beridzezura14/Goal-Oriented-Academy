def get_sum(a,b):
    if a == b:
        return a
    
    result = []

    if a < b:
        for i in range(a,b+1):
            result.append(i)
    if b < a:
        for i in range(b,a+1):
            result.append(i)
        
    return sum(result)

print(get_sum(2026,1476))