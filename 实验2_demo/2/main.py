# 需求：进入系统显示系统功能界面，功能如下：
# ①　添加学员
# ②　删除学员
# ③　修改学员信息
# ④　查询学员信息
# ⑤　显示所有学员信息
# ⑥　退出系统
# 系统共6个功能，用户根据自己需求进行选取

class Student:
    id = 0
    name = ""
    age = 0


if __name__ == '__main__':
    students = []
    print("""
        # ①　添加学员
        # ②　删除学员
        # ③　修改学员信息
        # ④　查询学员信息
        # ⑤　显示所有学员信息
        # ⑥　退出系统
    
    """)
    while True:
        num = int(input("请输入序号"))
        if num == 1:
            students.append("张三")
        if num == 2:
            print()
            students.remove("张三")
            print()
        if num == 3:
            print()
            for i, v in enumerate(students):
                print(f"编号{i + 1},姓名:{v}")
            id = int(input("请输入学生的编号"))
            students[id - 1] = "李四"
            print()
        if num == 6:
            break
            pass
