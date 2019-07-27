import random
point = 0
while True:  
    num_1 = random.randint(-15, 15)
    num_2 = random.randint(-15, 15)
    sign_random = random.randint(0,3)
    sign = ''
    final_result = 0
    if sign_random == 0:
        sign = '+'
    if sign_random == 1:
        sign = '-'
    if sign_random == 2:
        sign = '*'
    if sign_random == 3:
        sign = '/'
    result_random = random.randint(0,1)
    print(result_random)
    if result_random == 0:
        if sign_random == 0:
            final_result = num_1 + num_2
        if sign_random == 1:
            final_result = num_1 - num_2
        if sign_random == 2:
            final_result = num_1 * num_2
        if sign_random == 3:
            final_result = num_1 / num_2
    else:
        final_result = final_result + 1
    print(num_1, sign, num_2, "=", final_result)
    answer = int(input("Enter your answer:"))
    
    if result_random == answer:
        print('correct')
        point = point + 1
    else:
        print('game over')
        print (point)
        break
    
    



   