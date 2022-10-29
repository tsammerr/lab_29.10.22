def print_rec(a, b):
    try:
        for i in range(0, a):
            for j in range(0,b):
                print(" * ", end="  ")
            print()

    except Exception as ex:
        print(f'Error information: {ex}')


print_rec(7, 7)
