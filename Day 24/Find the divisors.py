cc = "daadsfvksahdvfkajhsdgfkahsgdfkahsdgfkjashgfkajshdfkajsdhfahf"

x = len(cc) - 4
hide = x * "#"

show = cc[-4:]

# result = []
# for i in cc:
#     result.append(i)
# show = "".join(result[-4:]) 

print(hide+show)

# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]

# print(maskify(cc))