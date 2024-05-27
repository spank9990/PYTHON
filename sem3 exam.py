#....................section B..........................
#Q2(d)
# str = input("enter any string")

# for i in str:
#     print(i,end=",")

#Q2(e)      //////////////////////
# import matplotlib.pyplot as plt
# foods = ['Meat', 'Banana', 'Avocados', 'Sweet Potatoes', 'Spinach', 'Watermelon', 'Coconut water', 'Beans', 'Legumes', 'Tomato']
# calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
# potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
# fat = [8, 5, 3, 6, 0, 1.5, 0, 2, 1.5, 2.5]

# # Plotting
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plotting calories
# ax.bar(foods, calories, color='skyblue', label='Calories')

# # Plotting potassium
# ax.bar(foods, potassium, color='lightgreen', label='Potassium')

# # Plotting fat
# ax.bar(foods, fat, color='salmon', label='Fat')

# # Adding labels and title
# ax.set_xlabel('Food')
# ax.set_ylabel('Amount')
# ax.set_title('Nutritional Content of Foods')
# ax.legend()

# # Rotating x-axis labels for better visibility
# plt.xticks(rotation=45, ha='right')

# # Show plot
# plt.tight_layout()
# plt.show()

#.......................  Section C.....................
#Q3(a),,,,,,,,,,,,

# def removenth(s,n):
#     x = len(s)
#     if n>=x:
#         return s
#     else:
#         str1 = s[:n]
#         str2 = s[n+1:]
#         str3 = str1 + str2
#         return str3
# print(removenth("MANGO",2))
# print(removenth("MANGO",7))

# Q3(b).........................
# def sort_words(input_string):
#     words = [word.strip() for word in input_string.split(',')]
#     sorted_words = sorted(words)
#     sorted_string = ", ".join(sorted_words)
#     return sorted_string

# input_sequence = input("Enter a comma-separated sequence of words: ")
# sorted_sequence = sort_words(input_sequence)
# print("Sorted words:", sorted_sequence)

#Q4(a)..................................
# import re

# def check_password(password):
#     if (6 <= len(password) <= 12 and
#             re.search("[a-z]", password) and
#             re.search("[0-9]", password) and
#             re.search("[A-Z]", password) and
#             re.search("[@#$", password)):
#         return True
#     else:
#         return False

# def validate_passwords(passwords):
#     valid_passwords = []
#     for password in passwords:
#         if check_password(password):
#             valid_passwords.append(password)
#     return valid_passwords

# # Get input from the user
# password_input = input("Enter a sequence of comma-separated passwords: ")

# # Split the input string by commas and remove any leading/trailing spaces
# passwords = [password.strip() for password in password_input.split(',')]

# # Validate the passwords and print the valid ones separated by commas
# valid_passwords = validate_passwords(passwords)
# print("Valid passwords:", ', '.join(valid_passwords))

#Q5(a),,,,,,,,,,,,,,,,,,,,,,,,,,,,..
# def ret_smaller(nested_list):
#     smallest = nested_list[0]
#     for sublist in nested_list:
#         if len(sublist) < len(smallest):
#             smallest = sublist
#     return smallest

# # Test case
# print(ret_smaller([[1, 2, 1.0, 0, 0, 12, 1, 2], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],[3,4,5]]))
# print(ret_smaller([[1, 2, 1, 0, 0, 12, 1, 2], ['a', 'b', 'c', 'J', 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))

#Q5(b)...................................
# import re

# def filter_numbers(text):
#     return re.sub(r'\d+', '', text)
# def filter_vowel_starting_strings(text):
#     return ' '.join(filter(lambda word: not re.match(r'^[aeiouAEIOU]', word), text.split()))
# def filter_specific_strings(text):
#     specific_strings = ['Agra', 'Ramesh', 'Tomato', 'Patna']
#     return ' '.join(filter(lambda word: all(specific not in word for specific in specific_strings), text.split()))

# def clean_text(text):
#     text = filter_numbers(text)
#     text = filter_vowel_starting_strings(text)
#     text = filter_specific_strings(text)
#     return text

# # Example usage:
# text = "123 Ramesh went to Agra. Tomato is a fruit. 456 Patna is a city."
# cleaned_text = clean_text(text)
# print(cleaned_text)

#Q6(a)..................................
# def number_to_text(num):
#     num_dict = {
#         '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
#     }
#     return ' '.join([num_dict[digit] for digit in str(num)])

# def product_within_limit(num1, num2):
#     product = num1 * num2
#     if product <= 10:
#         return number_to_text(product)
#     else:
#         return "The product exceeds the limit."

# # Example usage:
# num1 = 2
# num2 = 5
# result = product_within_limit(num1, num2)
# print("Given two integer numbers, return their product only if the product is equal to or lower than", result)

#Q6(b).....................................................
# def print_digit_words(file_name):
#     with open(file_name, 'r') as file:
#         words = file.read().split()

#     digit_words = [word for word in words if word.isdigit()]
    
#     if digit_words:
#         print("Words composed of digits only:")
#         for word in digit_words:
#             print(word)
#     else:
#         print("No words composed of digits found.")

# # Example usage:
# file_name = "A.txt"  # Replace "input.txt" with the name of your file
# print_digit_words(file_name)

#Q7(b)....................................................
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    while True:
        print("Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Calculator cleared.")
            elif choice == '6':
                print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Example usage:
calculator()