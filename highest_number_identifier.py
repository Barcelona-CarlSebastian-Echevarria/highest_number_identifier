# Prompt the user to input 5 numerical values
# Account for the attempts that will not satisfy the numerical input given without breaking or restarting the program
# Use a function with 5 variable parameteres to identify the highest numbers
# Assign the input variables to the funtion
# Run the program



# The first number disappears when the user didn't give a numerical value at the second prompt, this fixes that
def prompt(numerical_input):
    while True:
        try:
            ask_user = int(input("Enter a number: "))
            return ask_user
        except ValueError: 
            print("Please Enter a valid number")

# assigns the returned value to a variable
def variable_assignment():
    user_input1 = prompt("Enter a number: ")
    user_input2 = prompt("Enter a second number: ")
    return user_input1, user_input2

#The first two is working, however, this function is not being initiated for some reason
def find_the_highest_number(user_input1, user_input2):
    if user_input1 > user_input2:
        print(user_input1)
    else:
        print(user_input2)



user_input1, user_input2 = variable_assignment()
find_the_highest_number(user_input1, user_input2)

        
    