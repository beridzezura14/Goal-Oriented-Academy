# ნივთმა დაიკლო ფასში 10% ით,საიდანაც გამყიდველმა აიღო 8% მოგება, რამდენ % იან მოგებას აიღებდა ის ფასის დაკლებამდე?
# ჩაწერეთ ეს ყველა მონაცემი პითონში და დაათვლევინეთ მას. )))


prise = 80
percentage = 10
seller_percentage = 8

discount = prise * percentage / 100
print(discount)  # რამდენი ლარი დააკლდა 

result = prise - discount
print(result) # რამდენი ლარი იყო ნივთის ღირებულება ფასდაკლებით

seller_recive_monay = result * seller_percentage / 100
print(seller_recive_monay) # გამყიდველის მოგება

seller_recive_monay_2 = prise * seller_percentage / 100
# რამდენი ექნებოდა მოგება გამყიდველს რომარა ფასდაკლება
print("gamyidveli aiRebda " + str(seller_recive_monay_2) + " nacvlad " + str(seller_recive_monay) + " larisa") 