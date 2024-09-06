board={1:' ', 2:' ', 3:' ',
       4:' ', 5:' ', 6:' ',
       7:' ', 8:' ', 9:' '}
player="O"
bot="X"
def printBoard():
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('- + - + -')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('- + - + -')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('\n')

def isEmpty(position):
    if board[position]==' ':
        return True
    return False

def checkDraw():
    for key in board.keys():
        if board[key]==' ':
            return False
    return True



def checkWin():
    if(board[1]==board[2]==board[3] and board[1]!=' '):
        return True
    elif(board[4]==board[5]==board[6] and board[4]!=' '):
        return True
    elif(board[7]==board[8]==board[9] and board[7]!=' '):
        return True
    elif(board[1]==board[5]==board[9] and board[1]!=' '):
        return True
    elif(board[3]==board[5]==board[7] and board[3]!=' '):
        return True
    elif(board[1]==board[4]==board[7] and board[1]!=' '):
        return True
    elif(board[2]==board[5]==board[8] and board[2]!=' '):
        return True
    elif(board[3]==board[6]==board[9] and board[3]!=' '):
        return True
    else:
        return False
    
def insertMove(letter,position):
    if isEmpty(position):
        board[position]=letter
        printBoard()
        if checkWin():
            if letter==player:
                print("player won!")
                exit()
            else:
                print("bot won!")
                exit()
        if checkDraw():
            print("Draw")
            exit()
    else:
        print("this position is filled\n")
        position=int(input("Enter your position again:\n"))
        insertMove(letter,position)
    

def playerMove():
    position=int(input("Enter the position where you want to place O (1-9):\n"))
    insertMove(player,position)
    return

def compMove():
    bestScore=100
    bestPosition=0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score=minimax(board,False)
            board[key]=' '
            if score<bestScore:
                bestScore=score
                bestPosition=key
    insertMove(bot,bestPosition)
    return
        

def checkMarks(mark):
    if(board[1]==board[2]==board[3] and board[1]==mark):
        return True
    elif(board[4]==board[5]==board[6] and board[4]==mark):
        return True
    elif(board[7]==board[8]==board[9] and board[7]==mark):
        return True
    elif(board[1]==board[5]==board[9] and board[1]==mark):
        return True
    elif(board[3]==board[5]==board[7] and board[3]==mark):
        return True
    elif(board[1]==board[4]==board[7] and board[1]==mark):
        return True
    elif(board[2]==board[5]==board[8] and board[2]==mark):
        return True
    elif(board[3]==board[6]==board[9] and board[3]==mark):
        return True
    else:
        return False

def minimax(board,isMaximizing):
    if checkMarks(player):
        return 1
    elif checkMarks(bot):
        return -1
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore=100
        for key in board.keys():
            if(board[key]==' '):
                board[key]=bot
                score=minimax(board,False)
                board[key]=' '
                if score<bestScore:
                    bestScore=score
        return bestScore
    else:
        bestScore=-100
        for key in board.keys():
            if(board[key]==' '):
                board[key]=player
                score=minimax(board,True)
                board[key]=' '
                if score>bestScore:
                    bestScore=score
        return bestScore

printBoard()
while(not checkWin()):
    playerMove()
    compMove()

