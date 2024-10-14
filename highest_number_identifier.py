# Prompt the user to input 5 numerical values
# Account for the attempts that will not satisfy the numerical input given without breaking or restarting the program
# Use a function with 5 variable parameteres to identify the highest numbers
# Assign the input variables to the funtion
# Run the program



#Initial testing
def get_number():
    while True:
        try: 
            user_input1 = int(input("Enter a number: "))
            user_input2 = int(input("Enter a number: "))
            return user_input1, user_input2

        except ValueError:
            print("Enter a numerical value")
    

result1, result2 = get_number()
if result1 > result2:
    print(result1)
else:
    print(result2)

get_number()
        
    