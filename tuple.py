colours=("red","green","blue")

#creating a tuple with one item
# fruit=("apple",)
fruit=tuple(("apple"))
print(fruit)
#check type of tuple
print(type(fruit))

#check length of tuple
print(len(colours))

#accessing item in a tuple
print(colours[1])           #positive indexing
print(colours[-2])          #negative indexing
print(colours[1:3])         #range indexing
print(colours[-2:])        #negative range indexing

#check if an item in tuple
if "green" in colours:
    print("green in present in tuple")

#traverse of tuple
for i in colours:
    print(i)

#concatenate 2 tuple
# more_color=("skyblue","orange")
# colours=colours+more_color
# print(colours)

#unpacking a tuple
colors1, colors2, colors3 = colours
print(colors1,colors2,colors3) 
