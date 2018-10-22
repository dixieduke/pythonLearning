try:
    x = input('enter number: ')
    x = x + 1
    print(x)
except TypeError:
    print('invalid input!')
finally:
    print('valid input!')
    