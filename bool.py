# Define 'a' and 'b' variables as lists of integers
a = [5, 2, 3]
b = [2, 5, 3]

# The function compares two values
def compare(a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1


def print_result():
    # For loop that iterates over 'a' list and prints the result of comparison
    for i in range(len(a)):
        if a[i] > b[i]:
            print(f'{a[i]} > {b[i]}, hence return is', compare(a[i],b[i]))
        elif a[i] == b[i]:
            print(f'{a[i]} = {b[i]}, hence return is', compare(a[i],b[i]))
        else:
            print(f'{a[i]} < {b[i]}, hence return is', compare(a[i],b[i]))
    print("")

#A user inputs two nubers from the keyboard, which are compared by calling the function 'compare'
def user_input():
    user_input_a = int(input("Enter a: "))
    user_input_b = int(input("Enter b: "))
    print(f'\nYou entered {user_input_a} and {user_input_b}, hence return is', compare(user_input_a, user_input_b))

#Calling the print_result and user_input functions
print_result()
user_input()