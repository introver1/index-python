# Classes and Object
# Creating a Class
# class person:
#     name="santosh"
#     occupation="student"
#     age=20
#     def info(self):
#         print(f"{self.name} is a {self.occupation} and he is {self.age} yrs old.")
# a = person()
# b = person()
# c = person()
# b.name="arya"
# b.occupation="engineer"
# b.age=21
# c.name="hero"
# c.occupation="labour"
# c.age=21
# a.info()    
# b.info()
# c.info()

# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("Adding new name.")
# s1=Student('Raju')
# s2=Student('Rohan')
# s3=Student('Rakesh')
# s4=Student('Rockey')
# s5=Student('Rolex')
# print(s1.name)
# print(s2.name)
# print(s3.name)
# print(s4.name)
# print(s5.name)

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def average(self):
        sum=0
        for mar in self.marks:
            sum+=mar
            avg=mar/3
        print("Hi,",self.name,"you have score",avg)  

s1=student("Raja beta", [12,23,43])        
s1.average()  


class student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def info(self):
        print(f"{self.name} is a {self.gender}.")
s1=student("raja","boy")
s2=student("rani","girl")
s1.info()
s2.info()            