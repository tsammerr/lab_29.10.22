def print_biggest(a, b):
    try:
        if a > b:
            print(f'{a} is bigger then {b} ')
        if a < b:
            print(f'{b} is bigger then {a} ')
        elif a == b:
            print(f'{a} is equal to {b}')


    except Exception as ex:
        print(f'Error information: {ex}')


print_biggest(2, 1)
