# შემოიტანეთ აპლიკანტის: სიმაღლე (>= 1,6 და <=2,3) წონა (>=55 და <= 130) ასაკი (>=18 და <=27), 
# თუ აპლიკანტის მონაცემები აკმაყოფილებს შესაბამის მთხოვნებს,მაშინ დაობეჭდოს 
# " გილოცავთ!, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში" 
# და თუ არ აკმაყოფილებს მაიშინ დაობეჭდოს "
# სამწუხაროდ თქვენი მონაცემები არ შესაბამება ჩვენს მოთხოვნებს"


height = int(input("Seiyvanet simagle: "))
weight = int(input("Seiyvanet wona: "))
age = int(input("Seiyvanet asaki: "))


if (height >= 160 and height <= 230) and (weight >= 50 and weight <= 130) and (age >= 18 and age <+ 27):
    print("Tqven daakmayofilet pirobebi da gaweuli xarT jarshi")
else:
    print("Tqven VER daakmayofilet pirobebi")