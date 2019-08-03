while True:
    print("CRUD summary")
    crud_list = ["C:creat","R:read","U:update","D:delete",]
    for i,crud_list in enumerate(crud_list):
        print(i,".",crud_list)
    print()
    choice = int(input("Your choose: "))
    items = ["AOV","LOL","Dota","CS:GO","Mentor:))"]
    if choice == 0:
        Us_Fa = input("Please enter your favorite:")
        items.append(Us_Fa)
        print (items)
    elif choice == 1:
        bl_len=len(items)
        if bl_len == 0:
            print("Blank list ")
        else:
            for items in items:
                print(items)
    elif choice == 2:
        print(items)
        Position=int(input("Position to update: "))
        Object = input("Update object: ")
        items[Position]=Object
    elif choice == 3:
        print(items)
        user_locate=int(input("Delete location: "))
        items.pop(user_locate)
    else:
        break
print(items)
