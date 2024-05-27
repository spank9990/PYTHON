#for converting character to upper case
# str="india gate"
# str2=str.upper()
# print(str2)

#for lowercase
# str3=str2.lower()
# print(str3)

#for capatalize of a string
# print(str.capitalize())

#for stripping/removing a string
# str4="       hello priyak!  "
# print(str4.strip())

#replace substring
# str5="hello world, this world is beautiful any world."
# print(str5.replace("world","earth",1))

#splitting strings
# str6 = "ria,sia,pia,mia, tia, gia"
# list = str6.split(",",3)
# print(list)

#concatenate strings
# str1="Hello"
# str2=" World!"
# print(str1+str2)

#string formatting
student_name = "Drashya"
student_marks = 95

str1 = "The student name is {s} and marks of {s} is {m}".format(s=student_name,m=student_marks)
print(str1)