import random
n = int(random.random()*100)
print(n)
if n < 30:
    print("Rainy")
elif 30 < n < 60:
    print("Cloudy")
else:
    print("Sunny")