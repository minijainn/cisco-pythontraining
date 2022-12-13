class student:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print(self.name)
        print(self.id)

s1=student("mini",101)
s1.display()