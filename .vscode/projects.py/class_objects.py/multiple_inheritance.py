class employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"The nameis {self.name}")


class dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"The name of dance is {self.dance}")

class dancer_employee(employee,dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name




o=dancer_employee("baily","sunny")
print(o.name,o.dance)
o.show()