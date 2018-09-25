class Clazz(object):

    def __init__(self, name, course, teacher=None, stu_list=[]):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.stu_list = stu_list

    def __str__(self):
        print(self.name, self.course, self.teacher, self.stu_list)
