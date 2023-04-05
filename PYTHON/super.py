class Parent_one:
    def message(self):
        print("parent_one")
class Parent_two(Parent_one):
    def message(self):
        super().message()#or we use Parent_one.message() 
        #super key word used to acess the methods from parent,sibiling class
        print("parent_two")
ob=Parent_two()
ob.message()