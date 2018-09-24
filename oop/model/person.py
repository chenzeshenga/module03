class Person(object):

    def __init__(self, username, pwd, name, gender, age):
        self.username = username
        self.pwd = pwd
        self.name = name
        self.gender = gender
        self.age = age


class Teacher(Person):

    def __init__(self):
        super().__init__(self.name, self.gender, self.age)


class Student(Person):

    def __init__(self):
        super().__init__(self.name, self.gender, self.age)
        # class info list
        self.__student_data = None

    @property
    def student_data(self):
        return self.__student_data

    @student_data.setter
    def student_data(self, value):
        self.__student_data = value
