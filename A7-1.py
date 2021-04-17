
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


a = {'s': 3, 'm': 5}
b = {'s': 2, 'm': 7}
c= mul(a, b)
print(c['s'], '/', c['m'])
c= sum(a, b)
print(c['s'], '/', c['m'])
c= minus(a, b)
print(c['s'], '/', c['m'])
c= div(a, b)
print(c['s'], '/', c['m'])
