class dictionary:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def delete(self):
        del self.b

d=dictionary()
print("before del")
print(d.__dict__)
d.delete()
print(d.__dict__)