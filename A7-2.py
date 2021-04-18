def sum(x, y):
    result = {'hr': x['hr'] + y['hr'], 'm': x['m'] + y['m'], 's': x['s'] + y['s']}
    if result['s'] > 59:
        result['m'] += 1
        result['s'] -= 60
    if result['m'] > 59:
        result['hr'] += 1
        result['m'] -= 60
    return result


def minus(x, y):
    result = {'hr': x['hr'] - y['hr'], 'm': x['m'] - y['m'], 's': x['s'] - y['s']}
    if result['s'] > 59:
        result['m'] += 1
        result['s'] -= 60
    if result['m'] > 59:
        result['hr'] += 1
        result['m'] -= 60
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
    if result['m'] < 0:
        result['hr'] -= 1
        result['m'] += 60
    return result


def sec2time(x):
    result = {'hr': x // 3600, 'm': None, 's': None}
    x = x % 3600
    result['m'] = x // 60
    x = x % 60
    result['s'] = x
    return result


def time2sec(x):
    a = {'hr': x['hr'] * 3600, 'm': x['m'] * 60, 's': x['s']}
    result = a['hr'] + a['m'] + a['s']
    return result


while True:
    print('1- addition two time')
    print('2- minus two time')
    print('3- second to time converter')
    print('4- time to second converter')
    print('5- exit')

    choice = int(input('choose what do you want?: '))
    if choice == 1:
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a number for time one: "))
        s = int(input("Enter a number for time one: "))
        a = {'hr': hr, 'm': m, 's': s}
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a number for time one: "))
        s = int(input("Enter a number for time one: "))
        b = {'hr': hr, 'm': m, 's': s}
        c = sum(a, b)
        print('the Addition of these two time is: ')
        print(c['hr'], ':', c['m'], ':', c['s'])
    elif choice == 2:
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a number for time one: "))
        s = int(input("Enter a number for time one: "))
        a = {'hr': hr, 'm': m, 's': s}
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a number for time one: "))
        s = int(input("Enter a number for time one: "))
        b = {'hr': hr, 'm': m, 's': s}
        c = minus(a, b)
        print('the minus of these two time is: ')
        print(c['hr'], ':', c['m'], ':', c['s'])
    elif choice == 3:
        hr = int(input("Enter a hour: "))
        m = int(input("Enter a number: "))
        s = int(input("Enter a number: "))
        a = {'hr': hr, 'm': m, 's': s}
        c = time2sec(a)
        print('the second is: ')
        print(c)
    elif choice == 4:
        a = int(input("Enter second: "))
        c = sec2time(a)
        print('the time is: ')
        print(c['hr'], ':', c['m'], ':', c['s'])
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')
