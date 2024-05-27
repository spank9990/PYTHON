names={"sia","mia","tia"}

#check length of set
print(len(names))

#check data type of a set
print(type(names))
print(names)

#accessing item of a set
for x in names:
    print(x)

#check if a item exit in a set
if "sia" in names:
    print("sia in present in a set")

#add an item in a set
# names.add("ria")
# print(names)

#add another sequence in a set
# name_list=["ria","kia"]
# names.update(name_list)
# print(names)

#remove an item from a set
# names.remove("sia")
# names.remove("ria")
names.discard("ria")  #this function will not throw an error if value is not present in a set 
print(names)

#joining two sets
s1={'a','b','c'}
s2={'d','e','a'}
print(s1,s2)

# s3=s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#keep only duplicate value
# s1.intersection_update(s2)
# print(s1)

#keep all value except duplicates
s1.symmetric_difference_update(s2)
print(s1)