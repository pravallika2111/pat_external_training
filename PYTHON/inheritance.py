"""class A:
    def message_a(self):
        print("class A")
class B(A):
    def message_b(self):
        print("class B")
class C(B):
    def message_c(self):
        print("class C")
ob=C()
ob.message_a()"""
########
"""
class Parent_one:
    def message(self):
        print("class parent one")
class Parent_two:
    def message(self):
        print("class Parent_two")
class C(Parent_one,Parent_two):#even the function name is same the class which invokes first executes first
                            #for this output is class parent one aand C(Parent_two,Parent_one,) output class Parent_two
    pass
ob=C()
ob.message()"""
#hybrid inheritance 
#1)combination of hierarchical and multiple 
class A:
    def message_a(self):
        print("class A")
class B:
    def message_b(self):
        print("class B")
class C(B,A):
    def message_c(self):
        print("class C")
class D(C):
    def message_d(self):
        print("class D")
class E(C):
    pass
obj=E()
obj.message_b()
