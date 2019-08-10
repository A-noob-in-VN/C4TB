# numbers = [1, 6, 78, 4, 9]
# for i in numbers:
#     if i %2 == 0:
#         print (i)

numbers = input('Enter 5 numbers randomly:')
print (numbers.split())
a = numbers.split() 
for i in a:
    b = int(i)
    if b %2 == 0:
        print (i,sep=',')