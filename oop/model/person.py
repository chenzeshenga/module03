import os
import pickle

from oop.conf import setting
from oop.model.course import Course
from oop.model.school import School
from oop.model.clazz import Clazz
from oop.model.score import Score


class Person(object):

    def __init__(self, name=None, role=None, pwd="pwd", is_login=False):
        self.name = name
        self.role = role
        self.pwd = pwd
        self.is_login = is_login

    def check(self):
        file_path = os.path.join(setting.BASE_DIR, "user", self.name)
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            data = pickle.load(f, encoding="UTF-8")
            f.close()
            if self.pwd == data.pwd:
                print("登录成功")
                return data
            else:
                print("密码输入错误")
                return False
        else:
            return False


class Teacher(Person):

    def __init__(self, name, role="teacher", pwd="pwd", is_login=False):
        self.name = name
        self.role = role
        self.pwd = pwd
        self.is_login = is_login

    def manager_class(self):
        clazz_path = os.path.join(setting.BASE_DIR, "school", "class")
        print("你所管理的班级是：")
        for filename in os.listdir(clazz_path):
            file_path = os.path.join(clazz_path, filename)
            if os.path.isfile(file_path):
                file = open(file_path, "rb")
                data = pickle.load(file, encoding="UTF-8")
                if data.teacher == self.name:
                    print(data.name)
        return True

    def teach(self):
        clazz_path = os.path.join(setting.BASE_DIR, "school", "class")
        print("当前的班级如下-->")
        for filename in os.listdir(clazz_path):
            file_path = os.path.join(clazz_path, filename)
            if os.path.isfile(file_path):
                file = open(file_path, "rb")
                data = pickle.load(file, encoding="UTF-8")
                print("班级名称-->%s\t班级课程-->%s" % (data.name, data.course))
        clazz_name = input("请输入您所要执教的班级名称-->")
        file_path = os.path.join(clazz_path, clazz_name)
        if os.path.exists(file_path):
            file = open(file_path, "rb")
            data = pickle.load(file, encoding="UTF-8")
            file.close()
            data.teacher = self.name
            file = open(file_path, "wb")
            pickle.dump(data, file)
            file.close()
        print("执教成功")
        return True

    def query_stu(self):
        clazz_path = os.path.join(setting.BASE_DIR, "school", "class")
        print("你所管理的班级是：")
        for filename in os.listdir(clazz_path):
            file_path = os.path.join(clazz_path, filename)
            if os.path.isfile(file_path):
                file = open(file_path, "rb")
                data = pickle.load(file, encoding="UTF-8")
                if data.teacher == self.name:
                    print(data.name)
                    print("当前班级的学生为%s" % data.stu_list)
        return True

    def update_score(self):
        clazz_path = os.path.join(setting.BASE_DIR, "user")
        stu_name = input("请输入您所要修改的学生姓名-->").strip()
        stu_claz = input("请输入学生所在的班级-->").strip()
        stu_score = input("请输入学生成绩-->").strip()

        stu_score_obj = Score(stu_name, stu_claz, stu_score)
        file_path = os.path.join(clazz_path, stu_name)
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            data = pickle.load(f, encoding="UTF-8")
            f.close()
            data.score.append(stu_score_obj)
            f = open(file_path, "wb")
            pickle.dump(data, f)
            f.close()
            print("修改成功")
        else:
            print("该学生不存在")
        return True


class Student(Person):
    def __init__(self, name, role="student", pwd="pwd", is_login=False, score=[]):
        self.name = name
        self.role = role
        self.pwd = pwd
        self.is_login = is_login
        self.score = score

    def register(self):
        print("-------学生注册-----------")
        name = input("请输入用户名-->").strip()
        pwd = input("请输入密码-->").strip()
        student_obj = Student(name, pwd)
        if not student_obj.check():
            file_path = os.path.join(setting.BASE_DIR, "user", name)
            f = open(file_path, "wb")
            pickle.dump(student_obj, f)
            f.close()
            print("注册成功")
        else:
            print("注册失败")
        return True

    def pay(self):
        clazz_path = os.path.join(setting.BASE_DIR, "school", "class")
        sum = 0
        print("你所在的班级如下-->")
        for filename in os.listdir(clazz_path):
            file_path = os.path.join(clazz_path, filename)
            if os.path.isfile(file_path):
                file = open(file_path, "rb")
                data = pickle.load(file, encoding="UTF-8")
                file.close()
                if self.name in data.stu_list:
                    course_path = os.path.join(setting.BASE_DIR, "school", data.course)
                    if os.path.exists(course_path):
                        f = open(course_path, "rb")
                        course = pickle.load(f, encoding="UTF-8")
                        print("班级名称-->%s\t班级课程-->%s\t课程费用-->%s" % (data.name, data.course, course.price))
                        sum += int(course.price)
        print("您总计需要支付%s" % sum)
        return True

    def choose(self):
        clazz_path = os.path.join(setting.BASE_DIR, "school", "class")
        print("当前的班级如下-->")
        for filename in os.listdir(clazz_path):
            file_path = os.path.join(clazz_path, filename)
            if os.path.isfile(file_path):
                file = open(file_path, "rb")
                data = pickle.load(file, encoding="UTF-8")
                file.close()
                print("班级名称-->%s\t班级课程-->%s" % (data.name, data.course))
        clazz_name = input("请输入您所要学习的班级名称-->")
        file_path = os.path.join(clazz_path, clazz_name)
        if os.path.exists(file_path):
            file = open(file_path, "rb")
            data = pickle.load(file, encoding="UTF-8")
            file.close()
            if self.name in data.stu_list:
                print("您已经在该班级学习")
                return True
            else:
                data.stu_list.append(self.name)
            file = open(file_path, "wb")
            pickle.dump(data, file)
            file.close()
        print("选择成功")
        return True


class Admin(Person):
    def __init__(self, name, role="admin", pwd="pwd", is_login=False):
        self.name = name
        self.role = role
        self.pwd = pwd
        self.is_login = is_login

    def create_teacher(self):
        name = input("请输入讲师名-->").strip()
        teacher = Teacher(name)
        file_path = os.path.join(setting.BASE_DIR, "user", name)
        if not os.path.exists(file_path):
            f = open(file_path, "wb")
            pickle.dump(teacher, f)
            f.close()
            print("讲师创建成功")
        else:
            print("该讲师已存在")
        return True

    def create_class(self):
        name = input("请输入班级名-->").strip()
        course = input("请输入课程名-->").strip()
        teacher = input("请输入讲师名-->").strip()
        tea_path = os.path.join(setting.BASE_DIR, "user", teacher)
        if not os.path.exists(tea_path):
            print("没有 %s 老师" % teacher)
            return True
        clazz = Clazz(name, course, teacher)
        file_path = os.path.join(setting.BASE_DIR, "school", "class", name)
        if not os.path.exists(file_path):
            f = open(file_path, "wb")
            pickle.dump(clazz, f)
            f.close()
            print("班级创建成功")
        else:
            print("该班级已存在")
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
