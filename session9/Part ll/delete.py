while True:
    items = ['red', 'blue', 'green', 'teal']
    for i,color1 in enumerate(items):
        print(i,color1)

    delete_color = input("Delete color number : ")

    if delete_color.isdigit() :
        num = int(delete_color)
        items.pop(num)
        print("Our color list : ")
        for i,color1 in enumerate(items):
            print(i,color1)
        break
    elif delete_color.isalpha() :
        word = delete_color
        items.remove(word)
        print("Our color list : ")
        for i,color1 in enumerate(items):
            print(i,color1)
        break 
    else:
        print("Try again")
        break