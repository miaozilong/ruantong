# 本案例模拟马戏团运行流程，按照菜单选择查看动物基本信息（本马戏团中动物演员包括但不限于海豚、猴子、狮子等）、随机观看表演、顺序观看表演等。
import random

if __name__ == '__main__':
    shows = [
        "表演1",
        "表演2",
        "表演3",
    ]
    # for i, v in enumerate(shows):
    #     print(f"{i + 1},,,,{v}")
    #
    random.shuffle(shows)
    print(shows)
