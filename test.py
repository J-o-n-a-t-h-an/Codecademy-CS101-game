def print_hello():
    print("hello world")

def print_no():
    print("no.")

list_of_functions = {1: "print_hello", 2: "print_no"}

def return_input(input):
    try:
        return (list_of_functions[input]())
    except KeyError:
        print("That is not an option, please try again.")


user_choice = input("Please make choice, 1 or 2 > ")

return_input(user_choice)