WPieces = 9 #number of pieces in white player's reserve
BPieces = 9 #number of pieces in black player's reserve
class Space:
    def __init__(self, surrounding = [None,None,None,None], data = ''):
        self.data = data # piece currently occupying the space; _ default, w or b when occupied
        self.surrounding = surrounding #spaces that can be moved to, starting at top then moving clockwise (top, right, bottom, left) spaces stored as[int layer, int index 1, int index 2] 3 is used as no space since out of bounds
    def setPiece(self, piece):
        self.data = piece

board = [[[Space([None,[0,0,1],[0,1,0],None],'_'),Space([[1,0,1],[0,0,2],None,[0,0,1]],'_'),Space([None,None,[0,0,1],[0,1,2]],'_')],
    [Space([[0,0,0],None,[0,2,0],[2,1,0]],'_'),Space([None,None,None,None],'*'),Space([[0,0,2],[2,1,2],[0,2,2],None],'_')],
    [Space([[0,1,0],[0,2,1],None,None],'_'),Space([None,[0,2,2],[1,2,1],[0,2,0]],'_'),Space([[0,1,2],None,None,[0,2,1]],'_')]],
    [[Space([None,[1,0,1],[1,1,0],None],'_'),Space([[2,0,1],[1,0,2],[0,0,1],[1,0,1]],'_'),Space([None,None,[1,0,1],[1,1,2]],'_')],
    [Space([[1,0,0],[0,1,0],[1,2,0],[2,1,0]],'_'),Space([None,None,None,None],'*'),Space([[1,0,2],[2,1,2],[2,2,2],[1,1,2]],'_')],
    [Space([[1,1,0],[1,2,1],None,None],'_'),Space([[0,2,1],[1,2,2],[2,2,1],[1,2,0]],'_'),Space([[1,1,2],None,None,[1,2,1]],'_')]],
    [[Space([None,[2,0,1],[2,1,0],None],'_'),Space([None,[2,0,2],[1,0,1],[2,0,0]],'_'),Space([None,None,[2,1,2],[2,0,1]],'_')],
    [Space([[2,0,0],[1,1,0],[2,2,0],None],'_'),Space([None,None,None,None],'*'),Space([[2,0,2],None,[2,2,2],[1,1,2]],'_')],
    [Space([[2,1,0],[2,2,1],None,None],'_'),Space([[1,2,1],[2,2,2],None,[2,2,0]],'_'),Space([[2,1,2],None,None,2,2,1],'_')]]]

def printBoard():
    print(board[2][0][0].data+"     "+board[2][0][1].data+"     "+board[2][0][2].data+
        "\n  "+board[1][0][0].data+"   "+board[1][0][1].data+"   "+board[1][0][2].data+
        "\n    "+board[0][0][0].data+" "+board[0][0][1].data+" "+board[0][0][2].data+
        "\n"+board[2][1][0].data+" "+board[1][1][0].data+" "+board[0][1][0].data+"   "+board[0][1][2].data+" "+board[1][1][2].data+" "+board[2][1][2].data+
        "\n    "+board[0][2][0].data+" "+board[0][2][1].data+" "+board[0][2][2].data+
        "\n  "+board[1][2][0].data+"   "+board[1][2][1].data+"   "+board[1][2][2].data+
        "\n"+board[2][2][0].data+"     "+board[2][2][1].data+"     "+board[2][2][2].data)

def movePiece():
    return 0

printBoard()
quit()