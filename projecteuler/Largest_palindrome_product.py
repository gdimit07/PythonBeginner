# Largest palindrome product
# Show HTML problem content 
# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(num):
    verification_list = []
    div=10
    while num!=0:
        verification_list.append(num%div)
        num=num-num%div
        div=div*10
    
    div=10
    for i in range(1,len(verification_list)):
        verification_list[i]=verification_list[i]/div
        div=div*10
    
    verification_list.reverse()
    print(verification_list)
    
check_palindrome(1234567)
# items = []
# items.append(num%10)
# num=num-num%10
# items.append(num%100/10)
# num=num-num%100
# items.append(num%1000/100)
# num=num-num%1000
# items.append(num%10000/1000)
# num=num-num%10000
# items.append(num%100000/10000)
# num=num-num%100000
# items.append(num%1000000/100000)
# num=num-num%1000000
# print(items)
# print(num)

#print(palindrome_list)