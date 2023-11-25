# დავალება 1)
# შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი.


number = [45, 24, 87, 55, 62, 16, 115, 200]
# number_sum = number[0] + number[1] + number[2] + number[3] + number[4] + number[5]  long way
number_sum = sum(number)  # short way 

print(number_sum)

for num in number:
    if num % 2 == 0:
        print(num, " ეს არის ლუწი")
    else:
        print(num, " კენტი")
