# Prompt the user to input 5 numerical values
# Account for the attempts that will not satisfy the numerical input given without breaking or restarting the program
# Use a function with 5 variable parameteres to identify the highest number
# Assign the input variables to the funtion
# The program must compare the inputs 1st & 2nd and 3rd & 4th simultaneously, then compare the values to the 5th.





# The preceding numbers disappear when the user didn't give a numerical value at the present prompt, this function solves that.
def prompt(numerical_input):
    while True:
        try:
            ask_user = int(input("Enter a number: "))
            return ask_user
        except ValueError: 
            print("Please Enter a valid number")


# Assigns the returned value to a variable
def variable_assignment():
    user_input1 = prompt("Enter a number: ")
    user_input2 = prompt("Enter a second number: ")
    user_input3 = prompt("Enter a third number: ")
    user_input4 = prompt("Enter a fourth number: ")
    user_input5 = prompt("Enter a fifth number: ")
    return user_input1, user_input2, user_input3, user_input4, user_input5


# Finds the highest number by simultaneously comparing the numbers at 1st and 2nd place and 3rd and 4th, then compares it to the 5th
def find_the_highest_number(user_input1, user_input2, user_input3, user_input4, user_input5):
    
    if user_input1 > user_input2:
        result1 = user_input1

    else:
        result1 = user_input2


    if user_input3 > user_input4:
        result2 = user_input3
    else:
        result2 = user_input4


    if result1 > result2:
        if result1 > user_input5:
            print(f"the highest number among the given is {result1}")
        else:
            print(f"the highest number among the given is {user_input5}")

    else:
        if result2 > user_input5:
            print(f"the highest number among the given is {result2}")
        else:
            print(f"the highest number among the given is {user_input5}")

user_input1, user_input2, user_input3, user_input4, user_input5 = variable_assignment()
find_the_highest_number(user_input1, user_input2, user_input3, user_input4, user_input5)

        
    