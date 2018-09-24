from oop.model.person import Person, Student, Admin, Teacher

user_data = None


def login(func):
    def inner(*args, **kwargs):
        global user_data
        print("请输入用户名密码进行登录:")
        name = input("请输入用户名-->").strip()
        pwd = input("请输入密码-->").strip()
        person = Person(name, pwd)
        user_data = person.check()
        if user_data and not user_data["is_login"]:
            user_data["is_login"] = True
            user_data["person"] = person
            return func(*args, **kwargs)

    return inner


def check_role(param):
    def _check_role(func):
        def inner(*args, **kwargs):
            role = user_data["role"]
            if role == param:
                return func(*args, **kwargs)
            else:
                print("当前用户无法进入这个菜单")

        return inner

    return _check_role


def back():
    global user_data
    user_data = None
    return False


@login
@check_role("student")
def student():
    exit_flag = True
    while exit_flag:
        print('''
--------------管理员视图---------------
                1.注册
                2.交学费
                3.选择班级
                4.返回并注销
---------------------------------------
        ''')
        choice = input("请输入您需要进行的活动-->")
        menu_dict = {
            "1": "student.register()",
            "2": "student.pay()",
            "3": "student.choose()",
            "4": "back()"
        }

        if choice in menu_dict:
            if user_data["person"]:
                user = user_data["person"]
                student = Student(user.name, user.pwd)
                exit_flag = eval(menu_dict[choice])


@login
@check_role("admin")
def admin():
    exit_flag = True
    while exit_flag:
        print('''
    --------------管理员视图---------------
                1.创建讲师
                2.创建班级
                3.创建课程
                4.创建学校
                5.返回并注销
    ---------------------------------------
            ''')
        choice = input("请输入您需要进行的活动-->")
        menu_dict = {
            "1": "admin.create_teacher()",
            "2": "admin.create_class()",
            "3": "admin.create_course()",
            "4": "admin.create_school()",
            "5": "back()"
        }
        if choice in menu_dict:
            if user_data["person"]:
                user = user_data["person"]
                admin = Admin(user.name, user.pwd)
                exit_flag = eval(menu_dict[choice])


@login
@check_role("teacher")
def teacher():
    exit_flag = True
    while exit_flag:
        print('''
    --------------管理员视图---------------
                    1.管理班级
                    2.选择班级上班
                    3.查看学生列表
                    4.修改学生成绩
                    5.返回并注销
    ---------------------------------------
                ''')
        choice = input("请输入您需要进行的活动-->")
        menu_dict = {
            "1": "teacher.manager_class()",
            "2": "teacher.teach()",
            "3": "teacher.query_stu()",
            "4": "teacher.update_score()",
            "5": "back()"
        }
        if choice in menu_dict:
            if user_data["person"]:
                user = user_data["person"]
                teacher = Teacher(user.name, user.pwd)
                exit_flag = eval(menu_dict[choice])
