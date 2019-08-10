scores = [1, 5, 7, 8,46, 90]
scores.sort(reverse=True)
print("Hign scores :")
for i,scores in enumerate(scores):
    print(i,'.',scores)
score1=[1, 5, 7, 8,46, 90]
newscore = int(input("Enter your new score :"))
print(type(newscore))
score1.append(newscore)
score1.sort(reverse=True)
print("Hign scores :")
for n in range(5):
    print(score1[n])
newscore2 = int(input("Enter your new score :"))
score1.append(newscore2)
score1.sort(reverse=True)
print("NEW High scores:")
for n in range(5):
    print(score1[n])
