import os
def check_for_winner(listXO,sign):
    print('checking for possible',sign,'match')
    #checking if match was achieved
    #checking all rows
    if listXO[0][0]==listXO[0][1]==listXO[0][2]=='X':
        print('1st row matches!')
        return(True)
    elif listXO[1][0]==listXO[1][1]==listXO[1][2]==sign:
        print('2nd row matches!')
        return(True)
    elif listXO[2][0]==listXO[2][1]==listXO[2][2]==sign:
        print('3rd row matches!')
        return(True)
    #checking columns
    elif listXO[0][0]==listXO[1][0]==listXO[2][0]==sign:
        print('1st column matches!')
        return(True)
    elif listXO[0][1]==listXO[1][1]==listXO[2][1]==sign:
        print('2nd column matches!')
        return(True)
    elif listXO[0][2]==listXO[1][2]==listXO[2][2]==sign:
        print('3rd column matches!')
        return(True)
    #checking diagonals
    elif listXO[0][0]==listXO[1][1]==listXO[2][2]==sign:
        print('1st diagonal matches!')
        return(True)
    elif listXO[0][2]==listXO[1][1]==listXO[2][0]==sign:
        print('2nd diagonal matches!')
        return(True)
    else:
        print('No match found!')
        return(False)
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
def initialize_multi():
    listXO=[ ['-','-','-'] for emptyList in range(3) ]
    return(listXO)
    # for row  in range(len(listXO)):
    #     for column in range(3):
    #         listXO[row][column]='-'
def display_multi(listXO):
    for row in listXO:
        print (row)
def validate_coordinates_content(listXO,x,y):
    # print('-----')
    # print(listXO[x][y])
    if listXO[x][y] == '-':
        return True
    else:
        return False
def replace_multi(listXO,x,y,sign):
    x=int(x)
    y=int(y)
    listXO[x][y]=sign

#listXO=[[],[],[]]
# mylist=[ ['-','-','-'] for emptyList in range(3) ]
# mylist[0][0]='test'
# mylist=[ ['-','-','-'] for emptyList in range(3) ]
# print(mylist)

gameon=True
c=0
x=-1
y=-1


listXO=initialize_multi()
#display_multi(listXO)
#exit()
while gameon:
    os.system('cls')
    print('Game status:')
    display_multi(listXO)
    
#Player X
    print('Player X\'s turn')
    x,y=get_coordinates()

    while validate_coordinates_content(listXO,x,y)==False:
        print('Coordinates already occupied. Please enter a new set.')
        x,y=get_coordinates()
    
    replace_multi(listXO,x,y,'X')
    display_multi(listXO)

    if check_for_winner(listXO, 'X') == True:
        print("Congratulations 'X', you won!")
        if game_on() == True:
            print('Initializing game...')
            listXO=initialize_multi()
        else:
            break


#Player O
    os.system('cls')
    print('Game status:')
    display_multi(listXO)
    print('Player O\'s turn')
    x,y=get_coordinates()

    while validate_coordinates_content(listXO,x,y)==False:
        print('Coordinates already occupied. Please enter a new set.')
        x,y=get_coordinates()
    
    replace_multi(listXO,x,y,'O')
    display_multi(listXO)

    if check_for_winner(listXO, 'O') == True:
        print("Congratulations 'O', you won!")
        if game_on() == True:
            print('Initializing game...')
            listXO=initialize_multi()    
        else:
            break