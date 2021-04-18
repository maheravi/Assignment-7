
def mul(x, y):
    result = {'s': x['s'] * y['s'], 'm': x['m'] * y['m']}

    return result


def sum(x, y):
    result = {'s': x['s'] * y['m'] + x['m'] * y['s'], 'm': x['m'] * y['m']}

    return result


def minus(x, y):
    result = {'s': x['s'] * y['m'] - x['m'] * y['s'], 'm': x['m'] * y['m']}

    return result


def div(x, y):
    result = {'s': x['s'] * y['m'], 'm': x['m'] * y['s']}

    return result


print('first input your two fraction')
s = int(input("Enter a numerator for variable one: "))
m = int(input("Enter a denominator for variable one: "))
a = {'s': s, 'm': m}
s = int(input("Enter a numerator for variable two: "))
m = int(input("Enter a denominator for variable two: "))
b = {'s': s, 'm': m}
while True:
    print('done! Now choose your action from the list below: ')
    print('1- multiplication two Fraction')
    print('2- Addition two Fraction')
    print('3- minus two Fraction')
    print('4- div two Fraction')
    print('5- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        c = mul(a, b)
        print('the multiplication of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 2:
        c = sum(a, b)
        print('the Addition of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 3:
        c = minus(a, b)
        print('the minus of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 4:
        c = div(a, b)
        print('the division  of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

