# 1. 点和圆的位置判断
# 	【案例描述】
# 判断点和圆的关系（圆内还是圆外），设计一个同心圆类和一个点类：点有两个实例属性，x坐标，y坐标；同心圆有一个实例属性：半径r；两个类属性:圆心x坐标，圆心y坐标；
import math


#


#
class Circle:
    x = 0
    y = 0

    def __init__(self, r):
        self.r = r


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_in_circle(circle, point):
    ret = False
    length = math.sqrt((point.x - circle.x) ** 2 + (point.y - circle.y) ** 2)
    if length < circle.r:
        ret = True
    return ret


if __name__ == '__main__':
    circle = Circle(1)
    point = Point(3, 3)
    in_circle = is_in_circle(circle, point)
    print()
