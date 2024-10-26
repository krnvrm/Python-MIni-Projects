import os
import time
def cls():
    os.system('cls')
def start():
    print("Welcome to Tic Tac Toe !!")
    print("This is a blah blah match of the classic tic tac toe game.")
    while True:
        x=input("Player 1 choose your input (O or X)...")
        if x.upper() in {'O','X'}:
            break
        else:
            print('Wrong input ! Enter again')
    cls()
    if x.upper()=='O':
        return {'p1':' O ','p2':' X '}
    else:
        return {'p1':' X ','p2':' O '}
def print_grid():
    global grid
    print('   |   |   ')
    print(grid[1],'|',grid[2],'|',grid[3],sep='')
    print('___|___|___')
    print('   |   |   ')
    print(grid[4],'|',grid[5],'|',grid[6],sep='')
    print('___|___|___')
    print('   |   |   ')
    print(grid[7],'|',grid[8],'|',grid[9],sep='')
    print('   |   |   ')
def game_logic():
    global grid
    x=start()
    print('So, Player 1 is,',x['p1'])
    print('And Player 2 is,',x['p2'])
    print('The keys, Q, W, E, A, S, D, Z, X and C can be used for inputting')
    cls()
    def game_mechanics(turn):
        global grid
        if grid[1]==grid[2]==grid[3] and grid[1] in [' X ',' O '] or grid[4]==grid[5]==grid[6] and grid[4] in [' X ',' O '] or grid[7]==grid[8]==grid[9] and grid[7] in [' X ',' O ']:
            print("Player",turn,"has won !")
            return False
        elif grid[1]==grid[4]==grid[7] and grid[1] in [' X ',' O '] or grid[2]==grid[5]==grid[8] and grid[2] in [' X ',' O '] or grid[3]==grid[6]==grid[9] and grid[3] in [' X ',' O ']:
            print("Player",turn,"has won !")
            return False
        elif grid[1]==grid[5]==grid[9] and grid[1] in [' X ',' O '] or grid[3]==grid[5]==grid[7] and grid[3] in [' X ',' O ']:
            print("Player",turn,"has won !")
            return False
        else:
            #are values non empty ?
            flag=True
            for i in grid:
                if grid[i]=='   ':
                    flag=False
            if flag:
                print('This is a tie !!!')
                return False
    def game_sequence(x):
        global grid
        gameover=True
        available={1,2,3,4,5,6,7,8,9}
        for i in range(1,10):
            corr={'q':1,'w':2,'e':3,'a':4,'s':5,'d':6,'z':7,'x':8,'c':9}
            print_grid()
            while True:
                inp=input('Enter input...')
                if inp.lower() not in corr:
                    print("Wrong input enter again")
                elif inp.lower() in corr and corr[inp.lower()] not in available:
                    print("Already used place, enter again")
                else:
                    print(available)
                    available.remove(corr[inp])
                    cls()
                    break
            if i%2!=0:
                grid[corr[inp]]=x['p1']
                gameover=game_mechanics(1)
            elif i%2==0:
                grid[corr[inp]]=x['p2']
                gameover=game_mechanics(2)
            if gameover==False:
                break
    game_sequence(x)
while True:
    grid={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   ',9:'   '}
    game_logic()
    x=input("Input X to close the program, any othe key to keep playing.")
    if x.lower()=='x':
        print("Thanks for playing, the program will auto close in 5 seconds.")
        time.sleep(5)
        break



        

            





        

     
    