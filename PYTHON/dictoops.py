class Bike:
    d={}
    def add(self,model,val):
        self.d[model]=val
    def enter(self):
        self.bike_name=input()
        
    def sold(self,model):
        del self.d[model]
    def print1(self,model):
        if model not in self.d:
            print("not available")
        else:
            print(self.d[model])
ob=Bike()
ob.add("r15","Price:150000")
ob.add("mt15","Price:190000")
ob.add("pulsar","Price:120000")
ob.add("continental","Price:200000")
a=ob.enter()
ob.print1(a)