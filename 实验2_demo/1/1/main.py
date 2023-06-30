def is_prime(num):
    ret = True
    for i in range(2, num):
        if num % i == 0:
            ret = False
    return ret


def goldbach_guess(num):

    for m in range(2, num):
        if is_prime(m):
            if is_prime(num - m):
                print(num, '=', m, '+', num - m)
                return True
    return False


if __name__ == '__main__':
    i = int(input("请从键盘上输入大于2的偶数"))
    if i % 2 != 0 or i <= 2:
        print("你输入的不是大于2的偶数")
    elif (goldbach_guess(i)):
        print("歌德巴赫猜想是不能证伪")
    else:
        print("哥德巴赫猜想不成立")
