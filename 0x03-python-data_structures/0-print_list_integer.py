def print_list_integer(my_list=[]):
    for num in my_list:
        if isinstance(num, int):
            print('{}'.format(num))
        else:
            print("Warning: Non-integer value found in the lisy.")
