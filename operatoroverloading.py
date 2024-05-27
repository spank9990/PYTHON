class ComplexNumbers:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        return ComplexNumbers(self.real+other.real , self.img+other.img)
    
c1 = ComplexNumbers(2,3)
c2 = ComplexNumbers(3,5)
c3 = c1+c2
print(c3.real,"+i",c3.img)
