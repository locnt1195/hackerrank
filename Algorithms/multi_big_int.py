# Libraries Included:
# Numpy, Scipy, Scikit, Pandas


def plus_big_int(a, b):
    a = a[::-1]
    b = b[::-1]
    len_a = len(a)
    len_b = len(b)
    greater = len_a > len_b and a or b
    smaller = len_a > len_b and b or a
    res = []
    num = 0
    for i in range(0, len(smaller)):
        s = int(a[i]) + int(b[i]) + num
        num = s > 9 and 1 or 0
        res.append(str(s % 10))
    # print('res', res)
    for i in range(len(smaller), len(greater)):
        s = int(greater[i]) + num
        num = s > 9 and 1 or 0
        res.append(str(s % 10))
    res = res[::-1]
    return ''.join(res)


def multi_big_int(a, b):
    a_negative, b_negative = False, False
    if a[0] == '-':
        a = a[1:]
        a_negative = True
    if b[0] == '-':
        b = b[1:]
        b_negative = True
    negative = (
        (a_negative and not b_negative) or
        (not a_negative and b_negative)) and '-' or ''
    result = '0'
    a = a[::-1]
    b = b[::-1]
    for index, value in enumerate(a):
        res = '0'
        for i2, val2 in enumerate(b):
            number = '%s%s' % (int(value) * int(val2), i2 > 0 and '0'*i2 or '')
            res = plus_big_int(number, res)
        res = '%s%s' % (res, i2 > 0 and '0'*index or '')
        result = plus_big_int(result, res)
    return '%s%s' % (negative, result)


res = multi_big_int('132312313', '-25123123123')
print(res == str(132312313 * -25123123123))
