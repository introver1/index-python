class employee:
    company = "Goolulu"
    def  show(self):
        print(f"The name of employee is {self.name} and the company name is {self.company}.")

    @classmethod
    def change_company(cls,newcompany):
        cls.company = newcompany

E1 = employee()
E1.name = "Introvert"
E1.show() 
E1.change_company("Nepal goolulu")   
E1.show() 
print(employee.company)


# Using Class method as Alternative Method


class person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    



e1 = person("Raja", 45000)
print(e1.name, e1.salary)

string = "Goli -25000"
e2 = person.fromstr(string)
print(e2.name)        
print(e2.salary)

# print(e2.name + str(e2.salary))



