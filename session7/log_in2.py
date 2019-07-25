username = input("Your username?")
print (username)
email = input("Your email address?")
print (email)
password = input("Your password?")
print (password)
request = input("Enter your password again")
print (request)
if request != password:
    print ("Please enter again")
else:
    print ("Done")