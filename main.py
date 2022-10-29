def num(n):
    print(f'Cube of the number {n} is: -> {n * n * n}')


try:
    num(5)
except Exception as ex:
    print(f'Error information: {ex}')
