color = ['red', 'blue', 'green']
print("Our color is :")
print(*color,sep=",")

more = input("Enter a new color : ")
print(more)
color.append(more)
print(*color,sep=", ")