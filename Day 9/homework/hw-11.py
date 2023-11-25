# User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, 
# თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუნტებში...
# (თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, დაუპრინტეთ რამდენი ფუტია ის.

user_height = int(input("Seiyvanet simagle: "))
wish = input("romel sidideSi gsurt tqveni simaRlis Cveneba airchiet: 'cm' tu 'ft': ")

choose_cm = "cm"
choose_ft = "ft"
ft = user_height * 0.03
cm = user_height * 1

if wish == choose_ft:
    print("tqveni simagle futebshi aris: " + str(ft) + "-ft")
if wish == choose_cm:
    print("tqveni simagle santimetrebshi arsis aris: " + str(cm) + "-cm")