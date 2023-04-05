from abc import ABC ,abstractmethod      #abc-abstract base class #ABC is abstract class
class Example(ABC):                      #it inherites ABC i.e abstract class so it became abstract class
    @abstractmethod
    def method_one(self):               #by mention @abstractmethod method became abstract method 
        print("HEllo1")                 #we cant's create object for andstract class
                                        #body should not be there for abstract method
                                        # #we can call by using simpe class
                                        #what ever you writ in abstract method it won;t execute
class Student(Example):
    def method_one(self):               #body is must ,method body is compulsary
        print("HEllo")
ob=Student()
ob.method_one()