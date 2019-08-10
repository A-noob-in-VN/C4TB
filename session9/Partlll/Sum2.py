numbers = input('Enter 4 numbers:')
print (numbers.split(' '))
a = numbers.split(' ') 
b = 0
for i in a:
    a = int(i)
    b = b + a
print (b)
# b =  a.split(',')
# print(b)
