f = open("A.txt","w")
f.write("hello! we are creating a new file.")
f = open("A.txt","a")
f.write(" this is more content in text file \n it is the second line")
f = open("A.txt","r")
# print(f.read(5))
# print(f.readline())
for x in f:
    print(x)

f.close()
f.open("A.txt")

import os
os.remove("A.txt")

print("file create successfully !...........")

# f = open("A.txt","x")
# f = open("A.txt","w")
# f.write("this is my first line.")
# f.close()
# f = open("A.txt","r")
# print(f.read(6))