#  magic/dunder method


class employee:
    def __len__(self, name,id):
        self.name = name
        self.id = id
      

    def __len__(self, name):
        self.name = name
        i=0
        for c in self.name:
            i+=1
            return i  

a = employee("introvert",2345)
print(a.name)
print(len(a))