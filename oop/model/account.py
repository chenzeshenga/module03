import hashlib
import json
import os
import pickle

from oop.conf import setting


class Account(object):
    user_data = {
        "username": None,
        "pwd": "",
        "is_login": False,
        "user_info": {}
    }

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def check(self):
        file_path = os.path.join(setting.BASE_DIR, "db", "account", self.name)
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            data = pickle.load(f, encoding="UTF-8")
            data = json.loads(data)
            if data["pwd"] == self.pwd:
                return True
            else:
                print("密码错误，请重新尝试")
                return False
        else:
            # print("用户%s不存在，请去注册" % self.name)
            return False

    @staticmethod
    def generate_md5(value):
        # md5_id = hashlib.md5()
        # md5_id.update(value.encode('utf-8'))
        return value
        # return md5_id.hexdigest()
