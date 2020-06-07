import random
boardpos=[" " for i in range(10)]
def playerinput(letter,pos):
    boardpos[pos]=letter


def board(boardpos):
    print("   |   |")
    print(" " + boardpos[1]+" "+"|"+" "+boardpos[2]+" "+"|"+" "+boardpos[3]+" ")
    print("___|___|___")
    print("   |   |")
    print(" " + boardpos[4] + " " + "|" + " " + boardpos[5] + " " + "|" + " " + boardpos[6] + " ")
    print("___|___|___")
    print("   |   |")
    print(" " + boardpos[7] + " " + "|" + " " + boardpos[8] + " " + "|" + " " + boardpos[9] + " ")
    print("   |   |")

def freespace(pos):
    return boardpos[pos]==" "
def isboardfull(boardpos):

    if boardpos.count(" ") > 1:
        return False
    else:
        return True


def winner(boardpos,letter):
    return ((boardpos[1]==boardpos[2]==boardpos[3]==letter) or \
    (boardpos[4]== boardpos[5]==boardpos[6]==letter) or \
    (boardpos[7]==boardpos[8]==boardpos[9]==letter) or \
    (boardpos[1]==boardpos[4]==boardpos[7]==letter) or \
    (boardpos[2]==boardpos[5]==boardpos[8]==letter) or \
    (boardpos[3]==boardpos[6]==boardpos[9]==letter) or \
    (boardpos[1]==boardpos[5]==boardpos[9]==letter) or \
    (boardpos[3]==boardpos[5]==boardpos[7]==letter))
def playermove():
    run=True
    while run==True:
        move=input("please enter the position u want to place your move between 1~9:")
        try:
            move=int(move)
            if move>0 and move<10:
                if freespace(move):
                    run=False
                    playerinput('X',move)
                else:
                    print("sorry space filled")
            else :
                print("please enter a number between 1 to 9")

        except:
            ("please type a number")

def compmove():
    possiblemove=[x for x,letter in enumerate(boardpos) if letter==" " and x!=0]
    move=0

    for sign in ["X","O"]:
        for i in possiblemove:
            boardcopy=boardpos[:]
            boardcopy[i]=sign
            if winner(boardpos,sign):
                move=i
                return move
    corners=[]
    for i in possiblemove:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move=selectRandom(corners)
        return move
    if 5 in possiblemove:
        move = 5
        return move
    edge=[]
    for i in possiblemove:
        if i in [2, 4 , 6, 8]:
            edge.append(i)
    if len(edge)>0:
        move=selectRandom(edge)
        return move

def selectRandom(lst):
    ln = len(lst)
    r=random.randrange(0,ln)
    return lst[r]

def mainlogic():
    print("welcome to the game")
    board(boardpos)
    while not(isboardfull(boardpos)):
         if not(winner(boardpos,"O")):
             playermove()
             board(boardpos)
         else:
             print("well you loose")
             break
         if not(winner(boardpos,"X")):
             move=compmove()
             if move==0 :
                 print(" ")
             else:
                 playerinput("O",move)
                 print("computer made its move")
                 board(boardpos)
         else :
             print("you win")
             break

    if isboardfull(boardpos):
         print("tie game")


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        boardpos = [' ' for x in range(10)]
        print('--------------------')
        mainlogic()
    else:
        break

