#abstraction:hiding the implementation
#SRS:software requirnment specification
#polymorphism:
# method overloading
# 1:operator overloading==>+ doing addition and concatenation
print(10+20)
print('mini'+' '+'jain')

class operatoroverloadingex:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        return self.name+other.name

    def __sub__(self, other):
        return self.name-other.name



o1=operatoroverloadingex("abhi")
o2=operatoroverloadingex("ikigai")

print(o1+o2)
#o1.__add__()

#-,*,/,%
#2:method overloading

class Methodoverloading:
    def m1(self):
        print("noth")
    def m1(self,a):
        print("one arg")
    def m1(selfself,a,b):
        print("2 args")

t=Methodoverloading()
#t.m1()
#t.m1(10)
t.m1(10,20)

#wild charecter:
class Methodoverloading:
    def sum(self,*a):
        sum=0
        for x in a:
            sum=sum+x
        print("sum: ",sum)

#*a:will grow on our request
# and dont kn no of args
o1=Methodoverloading()
o1.sum(10,30)




#constructor overloading:not possible
#same as method overloading
class Methodoverloading:
    def sum(self,*a):
        sum=0
        for x in a:
            sum=sum+x
        print("sum: ",sum)

#*a:will grow on our request
# and dont kn no of args
o1=Methodoverloading()
o1=Methodoverloading(10,20)