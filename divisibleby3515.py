number=int(input("enter any positive number:"))

if number % 15==0:
    print("number is divisible by 15.")
else:
    if number%3==0 or number%5==0:
        print("number is divisible by 3 OR 5 but not divisible by 15.")
    else:
        print("number is neither divisible by 3 OR 5 ")