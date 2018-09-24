class Course(object):

    def __init__(self, name, period, price, school, classList=[]):
        self.name = name
        self.period = period
        self.price = price
        self.school = school
        self.classList = classList

    def info(self):
        print("course info--> %s,%s,%s"
              % (self.name, self.price, self.classList))
        return self
