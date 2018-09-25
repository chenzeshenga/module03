import os
import pickle

from oop.conf import setting
from oop.model.person import Admin, Student, Teacher

# admin = Admin("admin")
stu = Student("stu1")
# teacher1 = Teacher("teacher1")
file_path = os.path.join(setting.BASE_DIR, "user", stu.name)
f = open(file_path, "wb")
pickle.dump(stu, f)
f.close()

# mock("admin", "admin")
# mock("stu1", "student")
# mock("teacher1", "teacher")
