import os
import pickle

from oop.conf import setting
from oop.model.course import Course
from oop.model.school import School


class Person(object):

    def __init__(self, name=None, pwd=None, is_login=False):
        self.name = name
        self.pwd = pwd
        self.is_login = is_login

    def check(self):
        file_path = os.path.join(setting.BASE_DIR, "user", self.name)
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            data = pickle.load(f, encoding="UTF-8")
            f.close()
            if self.pwd == data["pwd"]:
                print("登录成功")
                return data
            else:
                print("密码输入错误")
                return False
        else:
            return False


class Teacher(Person):
    def manager_class(self):
        print("manager_class")
        return True

    def teach(self):
        print("teach")
        return True

    def query_stu(self):
        print("query_stu")
        return True

    def update_score(self):
        print("update_score")
        return True


class Student(Person):
    def register(self):
        print("-------学生注册-----------")
        name = input("请输入用户名-->").strip()
        pwd = input("请输入密码-->").strip()
        student_obj = Student(name, pwd)
        if not student_obj.check():
            file_path = os.path.join(setting.BASE_DIR, "user", name)
            user_data2 = {
                "name": name,
                "pwd": pwd,
                "role": "student",
                "is_login": False
            }
            f = open(file_path, "wb")
            pickle.dump(user_data2, f)
            f.close()
            print("注册成功")
        else:
            print("注册失败")
        return True

    def pay(self):
        print("pay()")
        return True

    def choose(self):
        print("choose()")
        return True


class Admin(Person):
    def create_teacher(self):
        print("create_teacher")
        return True

    def create_class(self):
        print("create_class")
        return True

    def create_course(self):
        name = input("请输入课程名-->").strip()
        period = input("请输入课程周期-->").strip()
        price = input("请输入课程价格-->").strip()
        school = input("请输入课程所在学校-->").strip()
        course = Course(name, period, price, school)
        file_path = os.path.join(setting.BASE_DIR, "school", name)
        if not os.path.exists(file_path):
            f = open(file_path, "wb")
            pickle.dump(course, f)
            f.close()
            print("课程创建成功")
        else:
            print("该课程已存在")
        return True

    def create_school(self):
        name = input("请输入学校名-->").strip()
        city = input("请输入城市名-->").strip()
        school = School(name, city)
        file_path = os.path.join(setting.BASE_DIR, "school", name)
        if not os.path.exists(file_path):
            f = open(file_path, "wb")
            pickle.dump(school, f)
            f.close()
            print("学校创建成功")
        else:
            print("该学校已存在")
        return True
