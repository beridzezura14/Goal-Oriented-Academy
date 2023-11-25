# შექმენით თქვენი ფილმების სია, რომელშიც ჩაწერთ უკვე ნანახ ფილმებს.
# მომხმარებელს(თქვენს პირობით მეგობარს) შემოატანინეთ მის მიერ რეკომენდირებული ფილმი. 
# თუ ფილმი დაემთხვევა თქვენს სიაში არსებულ ფილმს დაწერეთ “ძალიან მომეწონა ეს ფილმი 
# ან არ მომეწონა ეს ფილმი” თუ არ გაქვს ნანახი “ჩავინიშნავ და აუცილებლად ვნახავ”


my_list = ["naruto", "game of throne", "vikings", "banshe", "attack on titan"]  # სია
future_list = []
print(my_list)

for i in range(2):
    friend = input("mirchie 2 filmi: ")

    if friend in my_list:   # როცა string-ს ადარებ სიის ელემენტებს გამოიყენება in ფუნქცია
        print("es filmi ukve nanaxi maqvss")
    else:
        print("aucileblad chaviniSnav da davamateb chems sias")
        future_list.append(friend)
        print("Senaxuli filmebis sia: " + str(future_list))
    i += 1