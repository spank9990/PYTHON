class parent:
    def __init__(self):
        self.super_attribute = True
        print("this is a parent class")

class child(parent):
    def __init__(self):
        super().__init__()
        print("this is a child class")
        print(self.super_attribute)


child1 = child()
