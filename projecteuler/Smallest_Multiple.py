# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#prime factors method to be used


def factorize_single(num):
    
    factorized_num = []

    if num == 1:
        factorized_num.append(1)
        return(factorized_num)

    i = 2

    while num != 1:

        if num%i == 0:
            factorized_num.append(i)
            num = num / i
        else:
            i = i + 1
    
    return(factorized_num)


all_nums_factorized = []
start=1
end=21
smallest_multiple = []
duplicate = []

for j in range(start,end):
    all_nums_factorized.append(factorize_single(j))

while len(all_nums_factorized) != 0:
    for a_list in all_nums_factorized:

        if len(a_list) == 0:
            all_nums_factorized.remove(a_list)
        elif len(a_list) == 1:
            duplicate = a_list
            all_nums_factorized.remove(a_list)

            for x in all_nums_factorized:
                if duplicate[0] in x:
                    x.remove(duplicate[0])

            smallest_multiple.append(duplicate[0])


print(smallest_multiple)

answer = 1

for i in smallest_multiple:
    answer =  answer * i



for i in range(1,21):
    print(answer,"/",i,"=",answer/i)


print("Smallest multiple: ",answer)