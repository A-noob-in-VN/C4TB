while True:
    txt = input("Enter a year of birth?")
    print (txt)
    if txt.isdigit():
        print ("A number")
        break
    else: 
        print ("Not a number")

print (2019 - int(txt))