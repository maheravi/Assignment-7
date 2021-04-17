# rp = real part & ip = imaginary part

def mul(x, y):
    result = {'rp': x['rp'] * y['rp'] - x['ip'] * y['ip'], 'ip': x['rp'] * y['ip'] + x['ip'] * y['rp']}

    return result


def sum(x, y):
    result = {'rp': x['rp'] + y['rp'], 'ip': x['ip'] + y['ip']}

    return result


def minus(x, y):
    result = {'rp': x['rp'] - y['rp'], 'ip': x['ip'] - y['ip']}

    return result


def div(x, y):
    a = y['rp'] ** 2 + y['ip'] ** 2
    print(a)
    result = {'rp': (x['rp'] * y['rp'] + x['ip'] * y['ip']) / a, 'ip': (x['ip'] * y['rp'] - x['rp'] * y['ip']) / a}

    return result


a = {'rp': 2, 'ip': 3}
b = {'rp': 4, 'ip': -5}

c= mul(a, b)
print(c['rp'], '+', c['ip'],'i')
c= sum(a, b)
print(c['rp'], '+', c['ip'],'i')
c= minus(a, b)
print(c['rp'], '+', c['ip'],'i')
c= div(a, b)
print(c['rp'], '+', c['ip'])
