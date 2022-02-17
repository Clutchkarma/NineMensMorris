P1Pieces = 9 #number of pieces in white player's reserve
P2Pieces = 9 #number of pieces in black player's reserve
class Space:
    def __init__(self, surrounding = [], data = ''):
        self.data = data # piece currently occupying the space
        self.surrounding = surrounding #spaces that can be moved to, starting at top then moving clockwise
    def setPiece(self, piece):
        self.data = piece

b1 = [[Space(),Space(),Space()],[Space(),Space(),Space()],[Space(),Space(),Space()]] #innermost board
b2 = [[Space(),Space(),Space()],[Space(),Space(),Space()],[Space(),Space(),Space()]] #middle board
b3 = [[Space(),Space(),Space()],[Space(),Space(),Space()],[Space(),Space(),Space()]] #outer board

quit()