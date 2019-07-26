username = input("Your username?")
print (username)
email = input("Your email address?")
print (email)
while True:
    password = input("Your password?")
    print (password)
    minimum_character = 8
    passlength = len(password)
    if passlength < minimum_character:
        print (Must have at least 8 characters)
    elif password.isalpha:
        print (Must include numbers)
    else:
        break
request = input("Enter your password again")
print (request)
if request != password:
    print ("Please enter again")
else:
    print ("Done")