def reverseString(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

user_input = input("Enter a string: ")
reversed_result = reverseString(user_input)
print("Reversed String:", reversed_result)