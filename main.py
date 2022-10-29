def simp(num)
    num = 7
    k = 0
    for item in range(2, num // 2 + 1):
        if num % item == 0:
            k = k + 1
    if k <= 0:
        print(f'{num} is simple')
    else:
        print(f'{num} is not simple')


try:

