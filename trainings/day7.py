"""class St:
    print("its class")
print(St,__doc__) #documentation ->describe the class
help(St) #describe the class"""
""" def getAdd(a,b):
    c=a+b"""# not expecting a and b from user

class st:
    def __init__(self,name,age,marks):#init will execute first
        self.name=name
        self.age=age
        self.marks=marks
        #self:if dont want to pass an argument pass self
        #can do the initalization purpose==>self initialize
        #how values are mapping init(self)[inbuilt] pass to self of talk
    def talk(self):
        print("hello i am ",self.name)
        print("i am ",self.age)
        print("i got ",self.marks)

#talk(self) why we are not able to call
#talk() isnt independent-->its associated with class

#st-->parent class,talk()-->child function,
#talk() function call-->go to parent for permission-->ask permission
#to call talk function take
#permission from student class
#2ways to take the permission


s1=st("mini",23,80)#reference of student class
s1.talk() #with the help of reference cal the function



