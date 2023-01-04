def sol(input):
    input = input.lower().split(' ')
    input = ''.join(input)
    my_dict = {}

    for char in input:
        my_dict[char] = my_dict.setdefault(char, 0) + 1

    print(my_dict)

    one_flag = True
    for item in my_dict.keys():
        if (my_dict[item] % 2 == 1 and one_flag):
            one_flag = False
        elif (my_dict[item] % 2 != 0):
            return False

    return True


print(sol("no x in nixon"))
