# Largest palindrome product
# Show HTML problem content 
# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def split_number(num):
    
    splitted_number = []

    while num >= 1:
        #get units
        splitted_number.append(int(num%10))
        #subtract the retrieved units from previous line
        num = num - (num%10)
        #divide the number by 10 to shift all digits by one position to the right 
        num = num/10
    
    return(splitted_number)

    
def is_palindrome(num):

    # even digit number
    if len(num)%2==0:
        while len(num) != 0:
            last_index = len(num)-1
            if num[0] == num[last_index]:
                #remove the last number first
                #e.g. 1234 -> if pop [0] first, the variable last_index will be out of range
                num.pop(last_index)
                num.pop(0)
                if len(num) == 0:
                    return True
            else:
                return False
    #odd digit number
    else:
        while len(num) != 1:
            last_index = len(num)-1
            if num[0] == num[last_index]:
                num.pop(last_index)
                num.pop(0)
                if len(num) == 1:
                    return True
            else:
                return False


largest=-1
largest_l=-1
largest_r=-1

for i in range(999,800,-1):
    for j in range(999,800,-1):
        if is_palindrome(split_number(i*j)) and i*j>largest:
            largest = i*j 
            largest_l = i
            largest_r = j
            

print(largest_l,"x",largest_r,"=",largest)