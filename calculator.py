n1=int(input("enter first number:"))
n2=int(input("enter Second number:"))

operator=input("enter operator")

match operator:
    case "+":print("sum is",n1+n2)
    case "-":print("difference is",n1-n2)
    case "*":print("multiplication is",n1*n2)
    case "/":print("division is",n1/n2)
    case _ :print("enter a valid operator")

