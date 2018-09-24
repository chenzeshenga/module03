import json
import os
import pickle

from oop.conf import setting
from oop.core.main import login
from oop.model.account import Account


class PageView(object):
    user_data = {
        "username": None,
        "pwd": "",
        "is_login": False,
        "user_info": {}
    }

    def __init__(self):
        self.menu = None
        self.__menu_dict = None
        self.account = None

    def change_password(self):
        username = self.user_data["username"]
        print("您将修改%s的密码" % username)
        oldPwd = input("请输入当前密码-->")
        newPwd = input("请输入新密码-->")

        account = Account(username, oldPwd)
        if account.check():
            file_path = os.path.join(setting.BASE_DIR, "db", "account", username)
            if os.path.exists(file_path):
                self.user_data["pwd"] = newPwd
                f = open(file_path, "wb")
                pickle.dump(self.user_data, f)
            else:
                print("该用户不存在")

    def back(self):
        return

    @property
    def menu_dict(self):
        return self.__menu_dict

    @menu_dict.setter
    def menu_dict(self, value):
        self.__menu_dict = value


class TeacherPage(PageView):
    pass


class StudentPage(PageView):

    def register(self):
        print("-------学生注册-----------")
        username = input("请输入用户名-->").strip()
        pwd = input("请输入密码-->").strip()
        account = Account(username, pwd)
        if not account.check():
            file_path = os.path.join(setting.BASE_DIR, "db", "account", username)
            self.user_data = {
                "username": username,
                "pwd": pwd,
                "is_login": False,
                "user_info": {}
            }
            f = open(file_path, "wb")
            pickle.dump(json.dumps(self.user_data), f)
            print("注册成功")
        else:
            print("注册失败")

    def pay(self):
        print("pay")
