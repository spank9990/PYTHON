n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))

# if n1>n2 and n1 >n3 :
#     print(n1,"is the greatest number")
# elif n2>n3 and n2>n1 :
#     print(n2,"is the greatest number")
# else:
#     print(n3,"is the greatest number")

#using nested if else statement 
if n1>n2:
    if n1>n3:
        print(n1,"is the greatest number")
    else:
        print(n3,"is the greatest number")
else:
    if n2>n3:
        print(n2,"is the greatest number")
    else:
        print(n3,"is the greatest number")
        