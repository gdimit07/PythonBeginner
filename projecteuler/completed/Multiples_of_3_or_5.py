# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

stopValue=1000
sum = 0 
my_list = [ item for item in range(1,stopValue) if item%3==0 or item%5==0 ]
for item in my_list:
   sum+=item

print(sum)