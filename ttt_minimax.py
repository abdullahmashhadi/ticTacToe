board = {   1:' ', 2:' ', 3:' ',
            4:' ', 5:' ', 6:' ',
            7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('- + - + -')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('- + - + -')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('\n')

        
def spaceIsFree(position):
    if(board[position]==' '):
        return True
    else:
        return False
    
def checkForDraw():
    for key in board.keys():
        if board[key]==' ':
            return False
    return True

def checkForWin():
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
    
def checkWhichMarkWon(mark):
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



def insertLetter(letter,position):
    if spaceIsFree(position):
        board[position]=letter
        printBoard(board)
        if checkForWin():
            if letter== "X":
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        if checkForDraw():
            print("Draw!")
            exit()

    else:
        print("Can't insert there!")
        position=int(input("Enter new position"))
        insertLetter(letter,position)
        return
player= 'O'
bot='X'

def playerMove():
    position=int(input("Enter the position for O: "))
    insertLetter(player,position)
    return

def compMove():
    bestScore= 800
    bestMove=0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score=minimax(board,0,False)
            board[key]=' '
            if(score<bestScore):
                bestScore=score
                bestMove=key
    insertLetter(bot,bestMove)
    return

def minimax(board,depth,isMaximizing):
    if checkWhichMarkWon(player):
        return 1
    elif checkWhichMarkWon(bot):
        return -1
    elif checkForDraw():
        return 0
    if isMaximizing:
            bestScore= 800
            for key in board.keys():
                if(board[key]==' '):
                    board[key]=bot
                    score=minimax(board,0,False)
                    board[key]=' '
                    if(score<bestScore):
                        bestScore=score
            return bestScore
    else:
        bestScore=-800
        for key in board.keys():
            if(board[key]==' '):
                board[key]=player
                score=minimax(board,depth+1,True)
                board[key]=' '
                if(score>bestScore):
                    bestScore=score
        return bestScore
    
turn=int(input("Welcome to Tic-Tac-Toe! Enter 1 if you want to go first, 2 if you want to go second:\n"))
printBoard(board)
while not checkForWin():
   if turn==2:
       compMove()
       playerMove()
   else:
       playerMove()
       compMove()