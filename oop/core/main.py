import sys

from oop.model.account import Account
from oop.model.pageView import StudentPage


def exit():
    print("再见")
    sys.exit()


def login():
    username = input("请输入用户名-->").strip()
    pwd = input("请输入密码-->").strip()
    account = Account(username, pwd)
    if account.check():
        account.user_data["is_login"] = True
        account.user_data["username"] = username
        print("登录成功")
    else:
        print("登录失败")


def run():
    while True:
        print('''
----------------欢迎登录选课系统---------------
        请输入您的身份
        1. 学生登录
        2. 教师登录
        3. 管理员登录
        4. 退出
        ''')
        menuDict = {
            "1": "student_page()",
            "2": "teacherPage()",
            "3": "adminPage()",
            "4": "exit()"
        }
        choice = input("请输入--》").strip()
        if choice in menuDict:
            # login()
            eval(menuDict[choice])
        else:
            print("输入错误，请重新输入")


def student_page():
    print("-------学生视图-------")
    print('''
        1.注册
        2.交学费
        3.选择班级
        4.返回
    ''')
    choice = input("请输入您需要进行的活动-->")
    studentView = StudentPage()
    menu_dict = {
        "1": "register()",
        "2": "pay()",
        "3": "choose()",
        "4": "back()"
    }
    studentView.menu_dict = menu_dict
    if choice in menu_dict:
        menu = studentView.menu_dict[choice]
        eval("studentView." + menu)
    else:
        print("输入错误，请重新输入")
