# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import ceil

def check_prime(n):
    for i in range(2,n+1):
        if n%i==0 and n!=2:
            #print(n,'is not prime')
            return False
        
        #print(n,'is prime')
        return True

my_num = 600851475143
ceil_half = ceil(my_num/2)  # no need to check higher than half
result = -1

for i in range(2,ceil_half):
    # print(i)
    if check_prime(i) and my_num%i==0:
        result = i
        my_num=my_num/i
        #print(my_num)
    
    if my_num == 1:
        break
    

print(result)