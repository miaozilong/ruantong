# 本案例根据用户输入的红包总金额与红包个数，模拟线上发红包。
import random

if __name__ == '__main__':
    amount = 5
    count = 3
    wallet = [1] * count
    if amount > count:
        allocation = amount - count
        i = 0
        while True:
            randint = random.randint(0, allocation)
            allocation = allocation - randint
            wallet[i] = wallet[i] + randint
            i = i + 1
            if allocation == 0:
                break
            if i >= count:
                i = 0
    elif amount == count:
        pass
    else:
        print("金额数量没有红包多，请增加金额或者减少数量")
        pass
    print(wallet)
