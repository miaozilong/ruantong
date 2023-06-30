import random
import time
import numpy as np

if __name__ == '__main__':
    # 构造数据
    list_a = []
    for i in range(10 ** 8):
        list_a.append(random.random())
    # 计算使用Python耗时
    start = time.time_ns()
    result1 = sum(list_a)
    end = time.time_ns()
    print("python计算耗时:", end - start, "纳秒！", (end - start) / (10 ** 9), "秒")
    # 计算使用Numpy耗时
    arr_a = np.array(list_a)
    start = time.time_ns()
    result2 = np.sum(arr_a)
    end = time.time_ns()
    print("numpy计算耗时:", end - start, "纳秒！", (end - start) / (10 ** 9), "秒")
