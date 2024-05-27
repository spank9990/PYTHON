def pallindrome_str(str):
    
    #cleaning the string
    clean_str = (str.replace(" ","")).lower()
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str = input("enter a string:")
if pallindrome_str(str):
    print("it is a pallindrome string")
else:
    print("not a pallindrome string")
