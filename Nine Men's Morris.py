from shutil import move


WPieces = 9 #number of pieces in white player's reserve
BPieces = 9 #number of pieces in black player's reserve
class Space:
    def __init__(self, surrounding = [None,None,None,None], data = ''):
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

def printBoard():
    print(" _______________\n"+"| "+board[2][0][0].data+"     "+board[2][0][1].data+"     "+board[2][0][2].data+" |"+
        "\n|   "+board[1][0][0].data+"   "+board[1][0][1].data+"   "+board[1][0][2].data+"   |"+
        "\n|     "+board[0][0][0].data+" "+board[0][0][1].data+" "+board[0][0][2].data+"     |"+
        "\n| "+board[2][1][0].data+" "+board[1][1][0].data+" "+board[0][1][0].data+"   "+board[0][1][2].data+" "+board[1][1][2].data+" "+board[2][1][2].data+" |"
        "\n|     "+board[0][2][0].data+" "+board[0][2][1].data+" "+board[0][2][2].data+"     |"+
        "\n|   "+board[1][2][0].data+"   "+board[1][2][1].data+"   "+board[1][2][2].data+"   |"+
        "\n| "+board[2][2][0].data+"     "+board[2][2][1].data+"     "+board[2][2][2].data+" |\n")

def jumpPiece():
    return 0

def placePiece():
    return 0

def movePiece():
    loc = [3,0,0]
    pos = [3,0,0]
    curLoc = None
    pos = ''
    while True:
        loc[0] = int(input("Enter Layer: "))
        loc[1] = int(input("Enter y coordinate: "))
        loc[2] = int(input("Enter x coordinate: "))
        if ((loc[0] >= 0 or loc[0] <= 2) and (loc[1] >= 0 or loc[1] <= 2) and (loc[2] >= 0 or loc[2] <= 2)) and (board[loc[0]][loc[1]][loc[2]].getPiece() == 'w' or board[loc[0]][loc[1]][loc[2]].getPiece() == 'b'):
            curLoc = board[loc[0]][loc[1]][loc[2]]
            break
        print("Please pick a valid location")


    while True:
        pos = input("Pick piece movement direction, w,a,s,d: ")
        if pos == 'w' or pos == 'W':
            if curLoc.getSurround()[0] != None:
                board[curLoc.getSurround()[0][0]][curLoc.getSurround()[0][1]][curLoc.getSurround()[0][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
        elif pos == 'd' or pos == 'D':
            if curLoc.getSurround()[1] != None:
                board[curLoc.getSurround()[1][0]][curLoc.getSurround()[1][1]][curLoc.getSurround()[1][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
        elif pos == 's' or pos == 'S':
            if curLoc.getSurround()[2] != None:
                board[curLoc.getSurround()[2][0]][curLoc.getSurround()[2][1]][curLoc.getSurround()[2][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
        elif pos == 'a' or pos == 'A':
            if curLoc.getSurround()[3] != None:
                board[curLoc.getSurround()[3][0]][curLoc.getSurround()[3][1]][curLoc.getSurround()[3][2]].setPiece(curLoc.data)
                curLoc.setPiece('_')
                break
        print("Invalid move")

board[0][0][0].setPiece('b')
printBoard()
movePiece()
printBoard()
quit()