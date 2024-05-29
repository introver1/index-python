# # Public Access Specificier in Python
# class Student:
#     def __init__(self,name):
#         self.name=name
# a = Student("Raja")
# print(a.name)

# Private Access Modifier
class Student:
    def __init__(self,name):
        self.__name=name
a = Student("Raja")
# print(a.__name) cannot be access directly and can be access inderctly like this
print(a._Student__name)
print(a.__dir__())
# Protected Access Modifier
