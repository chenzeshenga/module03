import sys

from oop.core import function


def exit():
    print("欢迎使用，再见")
    sys.exit()


def run():
    while True:
        print('''
    ----------------欢迎登录选课系统---------------
                    请选择您的身份
                    1. 学生登录
                    2. 教师登录
                    3. 管理员登录
                    4. 退出
    ----------------------------------------------
        ''')
        menuDict = {
            "1": "function.student()",
            "2": "function.teacher()",
            "3": "function.admin()",
            "4": "exit()"
        }
        choice = input("请输入--》").strip()
        if choice in menuDict:
            eval(menuDict[choice])
        else:
            print("输入错误，请重新输入")
