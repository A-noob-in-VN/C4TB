import random
Items= ["AOV","LOL","Dota","Mentor"]
random_word = random.choice(Items)
random_list = list(random_word)
shuffle = random.sample(random_list,len(random_list))
print("Jumpled :")
for i in shuffle:
    print(i)
user_input = input("Your answer : ")
if user_input == random_word:
    print("Correct!!")
elif user_input != random_word:
    print("<<Incorrect!!>>")