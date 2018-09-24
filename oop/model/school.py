import os

from oop.conf import setting


class School:

    def __init__(self):
        self.__name = None
        self.__city = None
        self.__course_list = []

    def setter(self, name, city):
        if self.check(name):
            self.__name = name
            self.__city = city
            return self
        else:
            return False

    @property
    def course_list(self):
        return self.__course_list

    @course_list.setter
    def course_list(self, value):
        self.__course_list.append(value)

    def check(self, name):
        if not os.path.exists("%s/db/school/%s" % (setting.BASE_DIR, name)):
            return True
        else:
            print("学校%s已存在，你可以在修改学校菜单下进行修改" % name)
            return False
