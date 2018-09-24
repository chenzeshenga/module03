import os
import pickle

from oop.conf import setting


def mock(username, role):
    user_info = {
        "username": username,
        "pwd": "pwd",
        "is_login": False,
        "role": role
    }

    file_path = os.path.join(setting.BASE_DIR, "user", username)
    f = open(file_path, "wb")
    pickle.dump(user_info, f)
    f.close()


mock("admin", "admin")
mock("stu1", "student")
mock("teacher1", "teacher")
