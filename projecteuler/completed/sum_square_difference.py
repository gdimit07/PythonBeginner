# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

def sum_of_squares(x):

    result = 0
    
    for i in range(x+1):
        result =  result + i**2

    return result

def square_of_sums(x):

    result = 0

    for i in range(x+1):
        result =  result + i
    
    return result**2

my_range = 100
ssq = sum_of_squares(my_range)
sqs = square_of_sums(my_range)

print("result: ",sqs-ssq)
