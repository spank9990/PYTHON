def fibonacci(n):
    if n==1: #base case
        return 0
    elif n==2:  #base case
        return 1
    else:       
        return(fibonacci(n-1)+fibonacci(n-2))  #recursive case
    
n= int(input("enter the value of n:"))
for i in range (1,n+1):
    print(fibonacci(i))

    