class Space:
    def __init__(self, surrounding = [None,None,None,None], data = ''):#constructor,
        self.data = data # piece currently occupying the space; _ default, w or b when occupied
        self.surrounding = surrounding #spaces that can be moved to, starting at top then moving clockwise (top, right, bottom, left) spaces stored as[int layer, int index 1, int index 2] 3 is used as no space since out of bounds
    def setPiece(self, piece):
        self.data = piece
    def getPiece(self):
        return self.data
    def getSurround(self):
        return self.surrounding

board = [[[Space([None,[0,0,1],[0,1,0],None],'_'),Space([[1,0,1],[0,0,2],None,[0,0,0]],'_'),Space([None,None,[0,0,1],[0,1,2]],'_')],
    [Space([[0,0,0],None,[0,2,0],[1,1,0]],'_'),Space([None,None,None,None],'*'),Space([[0,0,2],[1,1,2],[0,2,2],None],'_')],
    [Space([[0,1,0],[0,2,1],None,None],'_'),Space([None,[0,2,2],[1,2,1],[0,2,0]],'_'),Space([[0,1,2],None,None,[0,2,1]],'_')]],
    [[Space([None,[1,0,1],[1,1,0],None],'_'),Space([[2,0,1],[1,0,2],[0,0,1],[1,0,0]],'_'),Space([None,None,[1,0,1],[1,1,2]],'_')],
    [Space([[1,0,0],[0,1,0],[1,2,0],[2,1,0]],'_'),Space([None,None,None,None],'*'),Space([[1,0,2],[2,1,2],[1,2,2],[0,1,2]],'_')],
    [Space([[1,1,0],[1,2,1],None,None],'_'),Space([[0,2,1],[1,2,2],[2,2,1],[1,2,0]],'_'),Space([[1,1,2],None,None,[1,2,1]],'_')]],
    [[Space([None,[2,0,1],[2,1,0],None],'_'),Space([None,[2,0,2],[1,0,1],[2,0,0]],'_'),Space([None,None,[2,1,2],[2,0,1]],'_')],
    [Space([[2,0,0],[1,1,0],[2,2,0],None],'_'),Space([None,None,None,None],'*'),Space([[2,0,2],None,[2,2,2],[1,1,2]],'_')],
    [Space([[2,1,0],[2,2,1],None,None],'_'),Space([[1,2,1],[2,2,2],None,[2,2,0]],'_'),Space([[2,1,2],None,None,[2,2,1]],'_')]]]

def PrintBoard():
    print(" _______________\n"+"| "+board[2][0][0].data+"     "+board[2][0][1].data+"     "+board[2][0][2].data+" |"+
        "\n|   "+board[1][0][0].data+"   "+board[1][0][1].data+"   "+board[1][0][2].data+"   |"+
        "\n|     "+board[0][0][0].data+" "+board[0][0][1].data+" "+board[0][0][2].data+"     |"+
        "\n| "+board[2][1][0].data+" "+board[1][1][0].data+" "+board[0][1][0].data+"   "+board[0][1][2].data+" "+board[1][1][2].data+" "+board[2][1][2].data+" |"
        "\n|     "+board[0][2][0].data+" "+board[0][2][1].data+" "+board[0][2][2].data+"     |"+
        "\n|   "+board[1][2][0].data+"   "+board[1][2][1].data+"   "+board[1][2][2].data+"   |"+
        "\n| "+board[2][2][0].data+"     "+board[2][2][1].data+"     "+board[2][2][2].data+" |\n")

def JumpPiece(player):
    loc = [3,0,0]
    curLoc = None
    pos = [3,0,0]
    while True:
        PrintBoard()
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
        if pos[0] >= 0 and pos[0] <= 2 and pos[1] >= 0 and pos[1] <= 2 and pos[2] >= 0 and pos[2] <= 2 and board[pos[0]][pos[1]][pos[2]].getPiece() == '_':
            board[pos[0]][pos[1]][pos[2]].setPiece(player)
            curLoc.setPiece('_')
            break
        print("Please pick a valid location")
    PrintBoard()

def PlacePiece(player):
    loc = [3,0,0]
    while True:
        PrintBoard()
        loc[0] = int(input("Enter Layer: "))
        loc[1] = int(input("Enter y coordinate: "))
        loc[2] = int(input("Enter x coordinate: "))
        if loc[0] >= 0 and loc[0] <= 2 and loc[1] >= 0 and loc[1] <= 2 and loc[2] >= 0 and loc[2] <= 2 and board[loc[0]][loc[1]][loc[2]].getPiece() == '_':
            board[loc[0]][loc[1]][loc[2]].setPiece(player)
            break
        print("Please pick a valid location")
    PrintBoard()

def MovePiece(player):
    loc = [3,0,0]
    curLoc = None
    pos = ''
    while True:
        PrintBoard()
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
            if curLoc.getSurround()[0] != None and board[curLoc.getSurround()[0][0]][curLoc.getSurround()[0][1]][curLoc.getSurround()[0][2]].getPiece() == '_':
                board[curLoc.getSurround()[0][0]][curLoc.getSurround()[0][1]][curLoc.getSurround()[0][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
            print("Invalid move")
        elif pos == 'd' or pos == 'D':
            if curLoc.getSurround()[1] != None and board[curLoc.getSurround()[1][0]][curLoc.getSurround()[1][1]][curLoc.getSurround()[1][2]].getPiece() == '_':
                board[curLoc.getSurround()[1][0]][curLoc.getSurround()[1][1]][curLoc.getSurround()[1][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
            print("Invalid move")
        elif pos == 's' or pos == 'S':
            if curLoc.getSurround()[2] != None and board[curLoc.getSurround()[2][0]][curLoc.getSurround()[2][1]][curLoc.getSurround()[2][2]].getPiece() == '_':
                board[curLoc.getSurround()[2][0]][curLoc.getSurround()[2][1]][curLoc.getSurround()[2][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
            print("Invalid move")
        elif pos == 'a' or pos == 'A':
            if curLoc.getSurround()[3] != None and board[curLoc.getSurround()[3][0]][curLoc.getSurround()[3][1]][curLoc.getSurround()[3][2]].getPiece() == '_':
                board[curLoc.getSurround()[3][0]][curLoc.getSurround()[3][1]][curLoc.getSurround()[3][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
            print("Invalid move")
        print("Invalid move")
    PrintBoard()

def main():
    WRPieces = 9 #number of pieces in white player's reserve
    WBPieces = 0 #number of white pieces on the board
    BRPieces = 9 #number of pieces in black player's reserve
    BBPieces = 0 #number of black pieces on the board
    curPlayer = 'w'#current player starting with white
    while True:
        PrintBoard()
        if curPlayer == 'w':
            print("White player's turn")
            if WRPieces != 0:
                PlacePiece(curPlayer)
            elif WBPieces > 3:
                MovePiece(curPlayer)
            else:
                JumpPiece(curPlayer)
            curPlayer = 'b'
        else:
            print("Black player's turn")
            if BRPieces != 0:
                PlacePiece(curPlayer)
            elif BBPieces > 3:
                MovePiece(curPlayer)
            else:
                JumpPiece(curPlayer)
            curPlayer = 'w'

if __name__ == "__main__":
    main()