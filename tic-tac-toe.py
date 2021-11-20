def check_for_winner(list_1,list_2,list_3,sign):
    #checking if match was achieved

    #checking all columns
    if list_1[0]==list_2[0]==list_3[0]==sign:
        return('1st column matches!')
    elif list_1[1]==list_2[1]==list_3[1]==sign:
        return('2nd column matches!')
    elif list_1[2]==list_2[2]==list_3[2]==sign:
        return('3rd column matches!')
    #checking rows
    elif list_1[0]==list_1[1]==list_1[2]==sign:
        return('1st row matches!')
    elif list_2[0]==list_2[1]==list_2[2]==sign:
        return('2nd row matches!')
    elif list_3[0]==list_3[1]==list_3[2]==sign:
        return('3rd row matches!')
    #checking diagonals
    elif list_1[0]==list_2[1]==list_3[2]==sign:
        return('1st diagonal matches!')
    elif list_3[0]==list_2[1]==list_1[2]==sign:
        return('2nd diagonal matches!')
    else:
        return('No match found!')
def initialize(list_1,list_2,list_3):
    for i in range(3):
        list_1.append('-')
        list_2.append('-')
        list_3.append('-')
def display(list_1,list_2,list_3):
    #print(list_1,'\n',list_2,'\n',list_3,'\n')
    print(list_1)
    print(list_2)
    print(list_3)
    
list_1=[]
list_2=[]
list_3=[]

initialize(list_1, list_2, list_3)
display(list_1, list_2, list_3)