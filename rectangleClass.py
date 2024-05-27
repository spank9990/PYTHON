class rectangle:

    def __init__(self,height,width):
        print(f"A rectangle is created with height: {height} and width: {width}")
        self.height = height
        self.width = width

    def set_dimensions(self, width , height):
        self.width = width
        self.height = height

    def area(self):
        area = self.height * self.width
        return area
    
    def perimeter(self):
        perimeter = 2*(self.height+self.width) 
        return perimeter

#creating objects
       
rectangle1 = rectangle(3,7)
rectangle2 = rectangle(10,15)
# rectangle1.set_dimensions(10,12)
# print("height of rectangle is:",rectangle1.height)
# print("width of rectangle is:",rectangle1.width)
# print("area of rectangle is:",rectangle1.area())
# print("perimeter of rectangle is:",rectangle1.perimeter())



    
