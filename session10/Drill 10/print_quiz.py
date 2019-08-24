point = 0

Quiz = ['Quiz: Phát hành năm bao nhiêu?']
option = ['A.2019', 'B.2018', 'C.2017', 'D.2016']
print(Quiz)
print(option)
answer = ['A.2019']

choice = input('Enter your choice:')
if choice == answer[0]:
    print('True')
    point = point + 1
else:
    print('False')
    print(answer)


Quiz2 = ['Quiz: Tác giả tên gì?']
option2 = ['A.Shigeo Tokuda', 'B.Taishi Tsutsui', 'C.Tsukasa Fushimi', 'D.Hitsuji Tarou' ]
print(Quiz2)
print(option2)
answer2 = ['B.Taishi tsutsui']

choice2 = input('Enter your choice:')
if choice2 == answer2[0]:
    print('True')
    point = point + 1
else:
    print('False')

print(point, 'points')
if point == 1:
    print('50%')
elif point == 2:
    print('100%')
else:
    print ('0%', 'of correct answer')