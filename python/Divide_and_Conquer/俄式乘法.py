def multi(n, m):

    sum = 0
    if n == 0 or m == 0:
        return 0
    if n == 1:
        return m
    
    while n > 1:
        if n % 2 == 1:
            n >>= 1
            sum += m
            m <<= 1
        else:
            n >>= 1
            m <<= 1
    
    sum += m
    return sum

if __name__ == "__main__":
    print(multi(201, 30))
    print(201*30)
