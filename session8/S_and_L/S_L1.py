Items = ['N','Y','c']
user_input = input("Name your things : ")
user_things = user_input.split(',')
print(user_things)
for thing in user_things:
    print(thing)