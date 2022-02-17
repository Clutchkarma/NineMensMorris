P1Pieces = 9 #number of pieces in white player's reserve
P2Pieces = 9 #number of pieces in black player's reserve

class Space:
    def __init__(self):
        self.data = '' #piece currently occupying the space
        self.surrounding = [["",0,0],["",0,0],["",0,0],["",0,0]] #spaces that can be moved to, starting at top then moving clockwise
    def __init__(self, surrounding):
        self.data = '' # piece currently occupying the space
        self.surrounding = surrounding #spaces that can be moved to, starting at top then moving clockwise

b1 = [['','',''],['','',''],['','','']]#innermost board
b2 = [['','',''],['','',''],['','','']]#middle board
b3 = [['','',''],['','',''],['','','']]#outer board