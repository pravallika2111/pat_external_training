"""class contructor:
    def __init__(self):
        self.name = "charles"
        print("this is a constructor")
    def say_hello(self):
        print(self.name)#even the element in constructor it read even it not in class by default it treat as class variable
        
obj=contructor()
obj.say_hello()"""
#exp1
""" class Student:
    def __init__(self):
        self.arr=[]
    def add(self,val):
        self.arr.append(val)
    def print(self):
        print(self.arr)
ob=Student()
ob.add(10)
ob.print() 
obj=Student() #when ever we create a new obj the new array is called 
obj.print()"""
#exp2
class Student:
    arr=[]
    def add(self,val):
        self.arr.append(val)
    def print(self):
        print(self.arr)
ob=Student()
ob.add(10)
ob.print() 
#even we create new object it invokes the olb array only
obj=Student()
obj.print()