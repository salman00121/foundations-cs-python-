def filter_even_numbers(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers


try:
    input_list = input("Enter a list of integers separated by spaces: ")
    input_list = input_list.split()
    input_list = [int(x) for x in input_list]
    
    even_numbers_result = filter_even_numbers(input_list)
    
    if even_numbers_result:
        print("Even numbers from the list:", even_numbers_result)
    else:
        print("No even numbers found in the list.")
except ValueError:
    print("An error occurred. Please enter a valid list of integers.")
