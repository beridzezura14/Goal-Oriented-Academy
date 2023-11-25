# დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
# რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 1 ქულა და 
# გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),

import random
# შევქმენით სია

name_list = ["dato", "nika", "zura", "giga", "ilo"]

dato = 0
nika = 0
zura = 0
giga = 0
ilo = 0


# რანდომად გამოვიყვანთ და დავუსვამთ კითხვას
for i in range (len(name_list)):
    random_element = random.choice(name_list)
    name_list.remove(random_element)

    print("random person is: " + str(random_element))
    questionn = (input("ramdenia 2 * 2: "))
    ansver = "4"

    if questionn == ansver:
        if random_element == "dato":
            dato += 1            
    if questionn == ansver:
        if random_element == "nika":
            nika += 1            
    if questionn == ansver:  
        if random_element == "zura":
            zura += 1            
    if questionn == ansver:
        if random_element == "giga":
            giga += 1            
    if questionn == ansver:
        if random_element == "ilo"  :
            ilo += 1  
# თუ მათი პასუხი იყო სწორი გამოტანს 1_ს თუ არა გამოტანს 0-ს

correcct_ansver = 10
incorrect_ansver = 5

dato_point = 50
nika_point = 50
zura_point = 50
giga_point = 50
ilo_point = 50
# პასუხი თუ იყო 1 ესეიგი მისი პასუხი სწორია და დაემატება 10
# პასუხი თუ იყო 0 ესეიგი პასუხი არასწორია და გამოაკლდება 5

if dato == 1:
   print("datos pasuxi sworia")
   sum_point = dato_point + correcct_ansver
   print("daTos jamuri qulaa " + str(sum_point))
else:
    print("datos pasuxi arasworia")
    sum_point = dato_point - incorrect_ansver
    print("daTos jamuri qulaa " + str(sum_point))
# ---------------------------------------------------------------
if nika == 1:
   print("nikas pasuxi sworia")
   sum_point = dato_point + correcct_ansver
   print("nikas jamuri qulaa " + str(sum_point))
else:
    print("nikas pasuxi arasworia")
    sum_point = sum_point = nika_point - incorrect_ansver
    print("nikas jamuri qulaa " + str(sum_point))
# ---------------------------------------------------------------
if zura == 1:
   print("zuras pasuxi sworia")
   sum_point = zura_point + correcct_ansver
   print("zuras jamuri qulaa " + str(sum_point))
else:
    print("zuras pasuxi arasworia")
    sum_point = zura_point - incorrect_ansver
    print("zuras jamuri qulaa " + str(sum_point))
# ---------------------------------------------------------------
if giga == 1:
   print("gigas pasuxi sworia")
   sum_point = giga_point + correcct_ansver
   print("gigas jamuri qulaa " + str(sum_point))
else:
    print("gigas pasuxi arasworia")
    sum_point = giga_point - incorrect_ansver
    print("gigas jamuri qulaa " + str(sum_point))
# ---------------------------------------------------------------
if ilo == 1:
   print("ilos pasuxi sworia")
   sum_point = ilo_point + correcct_ansver
   print("ilos jamuri qulaa " + str(sum_point))
else:
    sum_point = ilo_point - incorrect_ansver
    print("ilos jamuri qulaa " + str(sum_point))
    
# საბოლოოდ გამოვიტანთ შედეგებს ვის ქონდა სწორი და ვის არასწორი ასევე ვის რამდენი ქულა აქვს
            