def true(a):
    try:
        if a > 0:
            print('true')
        if a < 0:
            print('false')

    except Exception as ex:
        print(f'Error information: {ex}')


true(-2)
