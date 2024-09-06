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
    winning_combinations=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for combination in winning_combinations:
        if board[combination[0]]==board[combination[1]]==board[combination[2]] and board[combination[0]]!=' ':
            return True
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
    winning_combinations=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for combination in winning_combinations:
        if board[combination[0]]==board[combination[1]]==board[combination[2]] and board[combination[0]]==mark:
            return True
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

