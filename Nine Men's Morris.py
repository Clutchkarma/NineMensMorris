#object representing a space on the game board
#attributes
#piece: a char representing what the space contains, either a playing piece ('w' or 'b') or empty ('o')
#surrounding: array of all spaces connected to this one, starting upward at index 0 and moving clockwise, (up, right, down, left)
class Space:
    def __init__(self, surrounding = [None,None,None,None], data = ''):
        self.data = data
        self.surrounding = surrounding
    def setPiece(self, piece):
        self.data = piece
    def getPiece(self):
        return self.data
    def getSurround(self):
        return self.surrounding

board = [[[Space([None,[0,0,1],[0,1,0],None],'o'),Space([[1,0,1],[0,0,2],None,[0,0,0]],'o'),Space([None,None,[0,0,1],[0,1,2]],'o')],
    [Space([[0,0,0],None,[0,2,0],[1,1,0]],'o'),Space([None,None,None,None],' '),Space([[0,0,2],[1,1,2],[0,2,2],None],'o')],
    [Space([[0,1,0],[0,2,1],None,None],'o'),Space([None,[0,2,2],[1,2,1],[0,2,0]],'o'),Space([[0,1,2],None,None,[0,2,1]],'o')]],
    [[Space([None,[1,0,1],[1,1,0],None],'o'),Space([[2,0,1],[1,0,2],[0,0,1],[1,0,0]],'o'),Space([None,None,[1,0,1],[1,1,2]],'o')],
    [Space([[1,0,0],[0,1,0],[1,2,0],[2,1,0]],'o'),Space([None,None,None,None],' '),Space([[1,0,2],[2,1,2],[1,2,2],[0,1,2]],'o')],
    [Space([[1,1,0],[1,2,1],None,None],'o'),Space([[0,2,1],[1,2,2],[2,2,1],[1,2,0]],'o'),Space([[1,1,2],None,None,[1,2,1]],'o')]],
    [[Space([None,[2,0,1],[2,1,0],None],'o'),Space([None,[2,0,2],[1,0,1],[2,0,0]],'o'),Space([None,None,[2,1,2],[2,0,1]],'o')],
    [Space([[2,0,0],[1,1,0],[2,2,0],None],'o'),Space([None,None,None,None],' '),Space([[2,0,2],None,[2,2,2],[1,1,2]],'o')],
    [Space([[2,1,0],[2,2,1],None,None],'o'),Space([[1,2,1],[2,2,2],None,[2,2,0]],'o'),Space([[2,1,2],None,None,[2,2,1]],'o')]]]

def printBoard():
    print(" _______________\n"+"| "+board[2][0][0].data+"-----"+board[2][0][1].data+"-----"+board[2][0][2].data+" |"+
        "\n| | "+board[1][0][0].data+"---"+board[1][0][1].data+"---"+board[1][0][2].data+" | |"+
        "\n| | | "+board[0][0][0].data+"-"+board[0][0][1].data+"-"+board[0][0][2].data+" | | |"+
        "\n| "+board[2][1][0].data+"-"+board[1][1][0].data+"-"+board[0][1][0].data+"   "+board[0][1][2].data+"-"+board[1][1][2].data+"-"+board[2][1][2].data+" |"
        "\n| | | "+board[0][2][0].data+"-"+board[0][2][1].data+"-"+board[0][2][2].data+" | | |"+
        "\n| | "+board[1][2][0].data+"---"+board[1][2][1].data+"---"+board[1][2][2].data+" | |"+
        "\n| "+board[2][2][0].data+"-----"+board[2][2][1].data+"-----"+board[2][2][2].data+" |\n ---------------")

def takePiece(piece):
    take = [3,3,3]
    while True:
        printBoard()
        take[0] = int(input("Enter Layer: "))
        take[1] = int(input("Enter y coordinate: "))
        take[2] = int(input("Enter x coordinate: "))
        if take[0] >= 0 and take[0] <= 2 and take[1] >= 0 and take[1] <= 2 and take[2] >= 0 and take[2] <= 2 and board[take[0]][take[1]][take[2]].getPiece() == piece:
            board[take[0]][take[1]][take[2]].setPiece('o')
            break
        print("Please pick a valid location")


def isThree(space: Space):
    opp = ''
    curspace = space
    curCheck = space.getSurround()[0]
    vert = True
    hor = True

    if space.getPiece() == 'w':
        opp = 'b'
    else:
        opp = 'w'

    #check upward
    if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece() and vert:
        curCheck = space.getSurround()[2]
        if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
            takePiece(opp)
            vert = False
        else:
            curCheck = space.getSurround()[0]
            curspace = board[curCheck[0]][curCheck[1]][curCheck[2]]
            curCheck = curspace.getSurround()[0]
            if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
                takePiece(opp)
                vert = False
    
    #check to right
    curCheck = space.getSurround()[1]
    if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece() and hor:
        curCheck = space.getSurround()[3]
        if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
            takePiece(opp)
            hor = False
        else:
            curCheck = space.getSurround()[1]
            curspace = board[curCheck[0]][curCheck[1]][curCheck[2]]
            curCheck = curspace.getSurround()[1]
            if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
                takePiece(opp)
                hor = False
    #check below
    curCheck = space.getSurround()[2]
    if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece() and vert:
        curCheck = space.getSurround()[0]
        if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
            takePiece(opp)
            vert = False
        else:
            curCheck = space.getSurround()[2]
            curspace = board[curCheck[0]][curCheck[1]][curCheck[2]]
            curCheck = curspace.getSurround()[2]
            if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
                takePiece(opp)
                vert = False

    #check to left
    curCheck = space.getSurround()[3]
    if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece() and hor:
        curCheck = space.getSurround()[1]
        if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
            takePiece(opp)
            hor = False
        else:
            curCheck = space.getSurround()[3]
            curspace = board[curCheck[0]][curCheck[1]][curCheck[2]]
            curCheck = curspace.getSurround()[3]
            if curCheck != None and board[curCheck[0]][curCheck[1]][curCheck[2]].getPiece() == space.getPiece():
                takePiece(opp)
                hor = False
            

def jumpPiece(player):
    loc = [3,0,0]
    curLoc = None
    pos = [3,0,0]
    print("Transporting piece")
    while True:
        printBoard()
        loc[0] = int(input("Enter Layer: "))
        loc[1] = int(input("Enter y coordinate: "))
        loc[2] = int(input("Enter x coordinate: "))
        if loc[0] >= 0 and loc[0] <= 2 and loc[1] >= 0 and loc[1] <= 2 and loc[2] >= 0 and loc[2] <= 2 and board[loc[0]][loc[1]][loc[2]].getPiece() == player:
            curLoc = board[loc[0]][loc[1]][loc[2]]
            break
        print("Please pick a valid location")

    while True:
        pos[0] = int(input("Enter Layer: "))
        pos[1] = int(input("Enter y coordinate: "))
        pos[2] = int(input("Enter x coordinate: "))
        if pos[0] >= 0 and pos[0] <= 2 and pos[1] >= 0 and pos[1] <= 2 and pos[2] >= 0 and pos[2] <= 2 and board[pos[0]][pos[1]][pos[2]].getPiece() == 'o':
            board[pos[0]][pos[1]][pos[2]].setPiece(player)
            curLoc.setPiece('o')
            break
        print("Please pick a valid location")
    printBoard()

def placePiece(player):
    loc = [3,0,0]
    print("Placing piece")
    while True:
        printBoard()
        loc[0] = int(input("Enter Layer: "))
        loc[1] = int(input("Enter y coordinate: "))
        loc[2] = int(input("Enter x coordinate: "))
        if loc[0] >= 0 and loc[0] <= 2 and loc[1] >= 0 and loc[1] <= 2 and loc[2] >= 0 and loc[2] <= 2 and board[loc[0]][loc[1]][loc[2]].getPiece() == 'o':
            board[loc[0]][loc[1]][loc[2]].setPiece(player)
            break
        print("Please pick a valid location")
    printBoard()

def movePiece(player):
    loc = [3,0,0]
    curLoc = None
    pos = ''
    print("Moving Pieces")
    while True:
        printBoard()
        loc[0] = int(input("Enter Layer: "))
        loc[1] = int(input("Enter y coordinate: "))
        loc[2] = int(input("Enter x coordinate: "))
        if ((loc[0] >= 0 and loc[0] <= 2) and (loc[1] >= 0 and loc[1] <= 2) and (loc[2] >= 0 and loc[2] <= 2)) and (board[loc[0]][loc[1]][loc[2]].getPiece() == player):
            curLoc = board[loc[0]][loc[1]][loc[2]]
            break
        print("Please pick a valid location")

    while True:
        pos = input("Pick piece movement direction, w,a,s,d: ")
        if pos == 'w' or pos == 'W':
            if curLoc.getSurround()[0] != None and board[curLoc.getSurround()[0][0]][curLoc.getSurround()[0][1]][curLoc.getSurround()[0][2]].getPiece() == 'o':
                board[curLoc.getSurround()[0][0]][curLoc.getSurround()[0][1]][curLoc.getSurround()[0][2]].setPiece(curLoc.data)
                curLoc.setPiece('o')
                break
            print("Invalid move")
        elif pos == 'd' or pos == 'D':
            if curLoc.getSurround()[1] != None and board[curLoc.getSurround()[1][0]][curLoc.getSurround()[1][1]][curLoc.getSurround()[1][2]].getPiece() == 'o':
                board[curLoc.getSurround()[1][0]][curLoc.getSurround()[1][1]][curLoc.getSurround()[1][2]].setPiece(curLoc.data)
                curLoc.setPiece('o')
                break
            print("Invalid move")
        elif pos == 's' or pos == 'S':
            if curLoc.getSurround()[2] != None and board[curLoc.getSurround()[2][0]][curLoc.getSurround()[2][1]][curLoc.getSurround()[2][2]].getPiece() == 'o':
                board[curLoc.getSurround()[2][0]][curLoc.getSurround()[2][1]][curLoc.getSurround()[2][2]].setPiece(curLoc.data)
                curLoc.setPiece('o')
                break
            print("Invalid move")
        elif pos == 'a' or pos == 'A':
            if curLoc.getSurround()[3] != None and board[curLoc.getSurround()[3][0]][curLoc.getSurround()[3][1]][curLoc.getSurround()[3][2]].getPiece() == 'o':
                board[curLoc.getSurround()[3][0]][curLoc.getSurround()[3][1]][curLoc.getSurround()[3][2]].setPiece(curLoc.data)
                curLoc.setPiece('o')
                break
            print("Invalid move")
        print("Invalid move")
    printBoard()

def main():
    WRPieces = 9 #number of pieces in white player's reserve
    WBPieces = 0 #number of white pieces on the board
    BRPieces = 9 #number of pieces in black player's reserve
    BBPieces = 0 #number of black pieces on the board
    curPlayer = 'w' #current player starting with white
    taken = False
    while True:
        printBoard()
        if curPlayer == 'w':
            print("White player's turn")
            if WRPieces != 0:
                placePiece(curPlayer)
                WRPieces -= 1
                WBPieces += 1
            elif WBPieces > 3:
                movePiece(curPlayer)
            else:
                jumpPiece(curPlayer)
            curPlayer = 'b'
        else:
            print("Black player's turn")
            if BRPieces != 0:
                placePiece(curPlayer)
                BRPieces -= 1
                BBPieces += 1
            elif BBPieces > 3:
                movePiece(curPlayer)
            else:
                jumpPiece(curPlayer)
            curPlayer = 'w'

#if __name__ == "__main__":
#    main()