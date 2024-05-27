input_string = input("enter string:")
N = int(input("enter value of N:"))

#creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[ : :-1]
dict1 = dict(zip(alphabets,reverse_alphabets))

#finding the part of string on which we will do mirror operation
prefix = input_string[0:N-1]
suffix = input_string[N-1: ]

#find the mirror string
mirror = ""
for i in range (0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
result = prefix + mirror
print("the result is:",result)