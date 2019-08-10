scores = [80,76,64,52,34,28]
print("the high scores :")
for i,score in enumerate(scores):
    print(i,'.',scores)
score1=[80,76,64,52,34,28]
newhighscore = int(input("Enter your new high score :"))
print(type(newhighscore))
score1.append(newhighscore)
print("Hign scores :")

for n,score2 in enumerate(score1):
    print(n,'.',score2)