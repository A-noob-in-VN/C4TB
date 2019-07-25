username = input("Your username?")
print (username)

import re

email = input("Your email address?")
print (email)
if re.search:
    print ("Must have punctuation")
else:
    pass
password = input("Your password?")
print (password)
request = input("Enter your password again")
print (request)
if request != password:
    print ("Please enter again")
else:
    print ("Done")