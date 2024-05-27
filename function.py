#write a function
# def printHello ():
#     #body of function
#     print("Hello World!!")
# printHello()

#functions which takes 2 input and gives us sum of two numbers
def add(n1=0, n2=0):
    print("n1:",n1)
    print("n2:",n2)
    sum = n1+n2
    return sum

#positional arguments
# print("the sum of number is:",add(1,2))

#keyword arguments(named arguments)
# print("the sum of number is :",add(n2=5,n1=2))

#default arguments 
#print("the sum of number is :",add(3))

#arbitrary arguments
def addALLNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
# output = addALLNumbers(1,2,3,4,5,6,7)
# print("the sum is:",output)    

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)

studentInfo(name = "priyank",age = 22 ,city = "Ghaziabad")
studentInfo(name = "adarsh",age = 21 ,city = "Delhi")