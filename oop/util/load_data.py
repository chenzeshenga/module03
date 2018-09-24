import os
import pickle

from oop.conf import setting


def loadByUsername(username):
    file_path = os.path.join(setting.BASE_DIR, "db", "user", username)
    if os.path.exists(file_path):
        f = open(file_path, "rb")
        data = pickle.load(f, encoding="UTF-8")
        f.close()
        return data
    else:
        print("%s 不存在" % username)
        return None
