# Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.

# The Task
# Think of a way to store the languages as a database. The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language', with a type String, and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.


# lang = [ ("english", "Welcome")
# , ("czech", "Vitejte")
# , ("danish", "Velkomst")
# , ("dutch", "Welkom")
# , ("estonian", "Tere tulemast")
# , ("finnish", "Tervetuloa")
# , ("flemish", "Welgekomen")
# , ("french", "Bienvenue")
# , ("german", "Willkommen")
# , ("irish", "Failte")
# , ("italian", "Benvenuto")
# , ("latvian", "Gaidits")
# , ("lithuanian", "Laukiamas")
# , ("polish", "Witamy")
# , ("spanish", "Bienvenido")
# , ("swedish", "Valkommen")
# , ("welsh", "Croeso")
# ]\

# language = "dutch"

# for i in range(0, len(lang)):
#     if lang[i][0] == language:
#         print(lang[i][1])

# # print(lang[1][1])





# data = [['a','b'], ['a','c'], ['b','d']]
# search = 'c'
# any(e[1] == search for e in data)

# print(any)


def greet(language):
    country = [("georgia", "gamarjoba")
            ,  ("english", "Welcome")
            , ("czech", "Vitejte")
            , ("danish", "Velkomst")
            , ("dutch", "Welkom")
            , ("estonian", "Tere tulemast")
            , ("finnish", "Tervetuloa")
            , ("flemish", "Welgekomen")
            , ("french", "Bienvenue")
            , ("german", "Willkommen")
            , ("irish", "Failte")
            , ("italian", "Benvenuto")
            , ("latvian", "Gaidits")
            , ("lithuanian", "Laukiamas")
            , ("polish", "Witamy")
            , ("spanish", "Bienvenido")
            , ("swedish", "Valkommen")
            , ("welsh", "Croeso")
            ]
    
    for i in range(0, len(country)):
        if country[i][0] == language:
            return country[i][1]
        
    return "Welcome"
    


print(greet("georgia"))