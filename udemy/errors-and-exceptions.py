#problem 1
for i in ['a','b','c']:
    try: #added
        print(i**2)
    except TypeError: #added
        print("Please check the type of the given values, they should be of type int!") #added

#problem 2
x = 5
y = 0

try: #added
    z = x/y
except ZeroDivisionError: #added
    print("Divide by zero is not a valid operation.") #added

#problem3
#Write a function that asks for an integer and prints the square of it. 
#Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            result = int(input("Please provide an integer:"))
        except:
            print("An error occured! Please try again!")
            continue
        else:
            print("Your number squared is:",result**2)
            break

ask()