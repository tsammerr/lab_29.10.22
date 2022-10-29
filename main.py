def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


try:
    n = 5
    print("The factorial of ", n, " is: ", fact(n))
except Exception as ex:
    print(f'Error information: {ex}')
