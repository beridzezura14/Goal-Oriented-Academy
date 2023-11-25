# დავალება 2)
# ბილეთი ღირს 25 ლარი, მაგრამ ბავშვებისთვის უფასოა, გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 

price_adult = 25
price_children = 0

adult = 18

people = int(input("people: "))   # 10
children = int(input("children: "))  # 3

adult_price = people * price_adult            # 10 * 25
children_price = children * price_children    # 3 * 0
sum = adult_price + children_price            # 250 + 0 

print("sul gadsaxadia", sum)                  # სულ საჭიროა 250