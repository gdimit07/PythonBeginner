import os
def check_for_winner(list_0,list_1,list_2,sign):
    #checking if match was achieved

    #checking all columns
    if list_0[0]==list_1[0]==list_2[0]==sign:
        return('1st column matches!')
    elif list_0[1]==list_1[1]==list_2[1]==sign:
        return('2nd column matches!')
    elif list_0[2]==list_1[2]==list_2[2]==sign:
        return('3rd column matches!')
    #checking rows
    elif list_0[0]==list_0[1]==list_0[2]==sign:
        return('1st row matches!')
    elif list_1[0]==list_1[1]==list_1[2]==sign:
        return('2nd row matches!')
    elif list_2[0]==list_2[1]==list_2[2]==sign:
        return('3rd row matches!')
    #checking diagonals
    elif list_0[0]==list_1[1]==list_2[2]==sign:
        return('1st diagonal matches!')
    elif list_2[0]==list_1[1]==list_0[2]==sign:
        return('2nd diagonal matches!')
    else:
        return('No match found!')
def initialize(list_0,list_1,list_2):
    for i in range(3):
        list_0.append('-')
        list_1.append('-')
        list_2.append('-')
def display(list_0,list_1,list_2):
    #print(list_0,'\n',list_1,'\n',list_2,'\n')
    print(list_0)
    print(list_1)
    print(list_2)
def game_on():
    choice=input('Do you want to continue playing?\nAnswer(Y/N):')

    while choice not in ['Y','N']:
        choice=input('Please provide a valid answer (Y/N).\nAnswer:')

    if choice == 'Y':
        return(True)
    else:
        return(False)
def get_coordinates():
    print('Please provide coordinates for your move.')

    x=input('X coordinate (Valid answers are 0,1 or 2):')
    while (x not in ['0','1','2']):
        x=input('X coordinate is not valid.\nPlease provide a valide X coordinate (0,1,2).\nAnswer:')


    y=input('Y coordinate (Valid answers are 0,1 or 2):')
    while (y not in ['0','1','2']):
        y=input('Y coordinate is not valid.\nPlease provide a valide Y coordinate (0,1,2).\nAnswer:')

    return(int(x),int(y))
def check_if_position_is_occupied(listXO,x,y):

    if listXO[x][y] != '-' :
        return(False)
    else:
        return(True)
def initialize_multi(listXO):
    init=['-','-','-']
    for i in range(3):
        listXO.append(init)
def display_multi(listXO):
    for row in listXO:
        print (row)


list_0=[]
list_1=[]
list_2=[]

listXO=[]

gameon=True
c=0
x=-1
y=-1

initialize_multi(listXO)
display_multi(listXO)