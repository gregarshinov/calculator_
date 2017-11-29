def mul(a, b):
    tail = len(a) - len(b)
    result = ''
    for i, j in zip(list(a), list(b)):
        result += i + j
    if tail > 0:
        result += a[-tail:]
    elif tail < 0:
        result += b[tail:]
    return result


print(mul('abcpc', 'xyz'))