txt = input ("Enter your password")
print (txt)
minimum_character = 8
passlength = len(txt)
if passlength < minimum_character:
    print ("Must have AT LEAST 8 characters")
elif txt.isalpha():
    print ("Must include a NUMBER")
else:
    print ("True")