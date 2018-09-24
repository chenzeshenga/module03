class Course(object):

    def __init__(self, name, price, classList=[], studentList=[]):
        self.name = name
        self.price = price
        self.classList = classList
        self.studentList = studentList

    def info(self):
        print("course info--> %s,%s,%s,%s"
              % (self.name, self.price, self.classList, self.studentList))
        return self
