class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num= self.num+n
    
    def sub(self, d, e):
        return d-e
    @staticmethod
    def add(a,b):
        return a + b

x=math(7)
print(x.num) 
x.addtonum(7)
print(x.num)      
print(x.sub(9,6))
print(math.add(8,9))