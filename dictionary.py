numbers = {
    "john" : 9837125578,
    "sia" : 9456826676,
    "harikant" : 5685659669
}

#printing a dictionary
# print(numbers)

#printing type of a dictionary
# print(type(numbers))

#print length of a dictionary
# print(len(numbers))

#access item in a dictionary
# print(numbers["john"])
# print(numbers.get("john"))
# print(numbers.keys())

#update value in a dintionary
# numbers["harikant"] = 1234567890
# print(numbers)

#adding element in dict
# numbers["ria"] = 45658974
# print(numbers)

more_numbers = {
    "kia" : 9562354200
}
numbers.update(more_numbers)
# print(numbers)

#remove element in dict
# numbers.pop("john")
# print(numbers)

# numbers.popitem()   #this remove last item of dict
# print(numbers)

# numbers.clear()  #this will doing empty the dict
# print(numbers)

#printing dict items 
# for x,y in numbers.items() :
#     print(x,y)
# for x in numbers.items() :
#     print(x)

#nested dictionaries
numbers={
    "Area1":{
        "a" : 1,
        "b" : 2,
        "c" : 3
    },
    "Area2" :{
        "x" :4,
        "y" :5,
        "z" :6
    }
}
print(numbers["Area1"]["a"])
print(numbers["Area2"]["y"])


