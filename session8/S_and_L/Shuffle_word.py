import random
input_word=input("Enter a word : ")
input_word_list = list(input_word)
print(input_word_list)
input_shuffle = random.sample(input_word_list,len(input_word_list))
print("Shuffled:")
for i in input_shuffle:
    print(i.upper())