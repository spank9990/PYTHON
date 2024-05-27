eng_marks=float(input("enter marks of english"))
math_marks=float(input("enter marks of maths"))
if eng_marks>80 and math_marks>80:
    print("grade A")
elif eng_marks>80 or math_marks>80:
    print("grade B")
else:
    print("grade C")