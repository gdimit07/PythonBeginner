# 10001st prime
# Show HTML problem content 
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def check_prime(n):
    for i in range(2,n+1):
        if n%i==0 and n!=2:
            print(n%i)
            print(n,'is not prime')
            return False
        
        print(n,'is prime')
        return True

target = 6
#target = 8

counter = 1
current = 1

# while True:
#     if check_prime(current):
#         if counter == target:
#             break
#         else:
#             counter = counter + 1
    
#     current = current + 1
    
#     print("current:",current,"counter:",counter)
# print("the 10 001st prime number is: ", current)

print(check_prime(9))