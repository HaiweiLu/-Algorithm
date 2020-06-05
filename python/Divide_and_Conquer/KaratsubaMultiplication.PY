def karatsuba(x, y):
    """大整数乘法,分治实现

    Arguments:
        x {int} -- number
        y {int} -- number
    """
    if x < 10 or y < 10:
        return x * y
    
    str_x = str(x)
    str_y = str(y)

    n = max(len(str_x), len(str_y))
    nby2 = n // 2

    # a = x / 10 ** (nby2)
    # b = x % 10 ** (nby2)
    # c = y / 10 ** (nby2)
    # d = y % 10 ** (nby2)

    # higher bits of each number
    x_h = int(str_x[:nby2])
    y_h = int(str_y[:nby2])

    # lower bits for each number here
    x_l = int(str_x[nby2:])
    y_l = int(str_y[nby2:])

    a = karatsuba(x_h, y_h)
    d = karatsuba(x_l, y_l)
    e = karatsuba(x_h + x_l, y_h + y_l) - a - d

    # ac = karatsuba(a, c)
    # bd = karatsuba(b, d)
    # ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

    return a * 10 ** len(str_x) + e * 10 ** (len(str_x) // 2) + d

def multi(x, y, n):
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        s = 1
    else:
        s = -1

    x, y = abs(x), abs(y)

    # if x < 10 or y < 10:
    #     return x * y
    if n == 1:
        if x == 1 and y == 1:
            return s
        else:
            return 0

    # n = max(len(str(x)), len(str(y)))
    nby2 = n // 2

    a = x / 10 ** (nby2)
    b = x % 10 ** (nby2)
    c = y / 10 ** (nby2)
    d = y % 10 ** (nby2)

    m1 = multi(a, c, n // 2)
    m2 = multi(a - b, d - c, n // 2)
    m3 = multi(b, d, n // 2)
    s *= (m1 * 10**nby2 + (m1 + m2 + m3) * 10**nby2 + m3)

    return s


def karatsubaMultiplication(x, y):
    """大整数乘法,分治实现"""
    x, y = str(x), str(y)

    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    
    n, j = len(x), len(x) // 2

    if (n % 2) != 0: j += 1

    BZeroPadding, AZeroPadding = n - j, (n - j) * 2
    a, b = int(x[:j]), int(x[j:])
    c, d = int(y[:j]), int(y[j:])

    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))

    return A + B + bd

def zeroPad(numberString, zeros, left = True):
    """补零"""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString


if __name__ == '__main__':
    print(karatsubaMultiplication(986722, 788889999))