# შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. დავპრინტოთ დაწყვილებულად 😄 
# აი დააკომენტარეთ და დაგაწყვილებთო რო იცოდნენ ფბზე ეგრე დაახლოებით  :დდდ

import random

# boy = ["zura", "levani", "dato", "nika"]
girl = ["qeti", "lana", "nia", "mariami"]

for i in range(4):
    name = input(("Seiyvane mocemuli saxelebi: "))
    print(name, random.choice(girl))



# roll_boy_1 = random.choice(boy)
# roll_girl_2 = random.choice(girl)
# print("pirvel datrialebaze dawyvildnen " + str (roll_boy_1) + " da " + str(roll_girl_2) )
