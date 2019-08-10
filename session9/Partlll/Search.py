numbers = [1, 6, 34, 90, 87]
def check_list():
    input_num = int(input("Enter a number: "))
    try:
        num_check=numbers.index(input_num)
    except ValueError:
        print("Not found in our list")
    else:
        print("found,position :",num_check)
check_list()