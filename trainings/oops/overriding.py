class parent:
    def property(self):
        print("gold+land")

class child(parent):
    def property(self):
        print("gold+silver+property+digify")

c=child()
c.property()