scores = [80,76,64,52,34,28]
scores.sort(reverse=True)
print("Hign scores :")
for i,score in enumerate(scores):
    print(i,'.',scores)
score1=[80,76,64,52,34,28]
newscore = int(input("Enter your new score :"))
print(type(newscore))
score1.append(newscore)
score1.sort(reverse=True)
print("Hign scores :")
for n,score2 in enumerate(score1):
    print(n,'.',score2)
    