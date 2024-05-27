fruits=["apple","mango","banana","cherry"]
print(fruits)

#sorting a list
# fruits.sort()           #by default ascending
# print(fruits)

#for reverse order of a list
# fruits.sort(reverse=True)     #descending 
# print(fruits)

# fruits.reverse()
# print(fruits)

#list comprehension
# new_fruits=[fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)

#copy a list
# new_fruits=fruits.copy()
# print(new_fruits)

# new_fruits = fruits+ new_fruits
# print(new_fruits)

#nested list
fruits.insert(2,["kiwi","papaya"])
print(fruits)
print(fruits[2][0])