def lcm(m, n):
    ret = 0
    for i in range(max(m, n), m * n + 1):
        if i % m == 0 and i % n == 0:
            ret = i
            break
    return ret


if __name__ == '__main__':
    lcm_number = lcm(3, 16)
    print(lcm_number)
