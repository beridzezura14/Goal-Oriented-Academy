# input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები

sentence = input("enter same sentence: ")

sentence_vowel = 0
sentence_Consonant = 0
other = 0

for i in sentence:
    # იპოვოს და გამოთვალოს ხმოვნების რაოდენობა
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        sentence_vowel += 1
    # თანხმოვნებს სფეისი ან სხვა სასვენი ნიშნები რომ არ მიამატოს
    elif i == " " or i == "." or i == "," or i == "-" or i == "?" or i == "!" or i == ":" or i == ";": 
        other += 1
    # იპოვოს და გამოთვალოს თანხმოვნების რაოდენობა  
    else:
        sentence_Consonant += 1

# გამოიტანოს შედეგი
print("winadadebaSi aris: " + str(sentence_vowel) + " xmovani")
print("winadadebaSi aris: " + str(sentence_Consonant) + " tanxmovani")
print("winadadebaSi aris: " + str(other) + " other")

