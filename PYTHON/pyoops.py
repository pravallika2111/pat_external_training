class Student:
    name='sai'
    age=21
    def say_hello(self,name):#self is to say that function is inside the class by this the compiler know that it is in the same class
            print("hello",name)
            print("hello",self.name)#when we use self.(dot) it check name from class variables where as when we print just name it print the name passed to function
ob=Student()
ob.say_hello('Sai Krishna')