class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def sayhi(self):
        print("hello i am",self.name,"and my id is ",self.id)

p1=person("nikhli",12)
p1.sayhi()


#Self variable:it is the default variable which always
# point to current value/object
# by using self we can access the instance and instance methods
#Note:1:self shld be the 1st parameter inside the constructor
#2:self shld be the first parameter inside the instance method:sayhi
#constructor concept:
#1:special method in python
#2:name of constructor:__init__
#3:constructor shld e executed automatically on run
#4:the main purpose of constructor is to declare the variable and initialization
#5:for each object there will be a unique constructor call.
#6:constructor can take atleast one argument--self
#7:constructor is optional if developer not providing python will automatically generate
