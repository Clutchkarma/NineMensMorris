P1Pieces = 9 #number of pieces in white player's reserve
P2Pieces = 9 #number of pieces in black player's reserve
class Space:
    def __init__(self, surrounding = [['',0,0],['',0,0],['',0,0],['',0,0]], data = ''):
        self.data = data # piece currently occupying the space
        self.surrounding = surrounding #spaces that can be moved to, starting at top then moving clockwise
    def setPiece(self, piece):
        self.data = piece

b1 = [[Space([],'_'),Space([],'_'),Space([],'_')],[Space([],'_'),Space([],'*'),Space([],'_')],[Space([],'_'),Space([],'_'),Space([],'_')]] #innermost board
b2 = [[Space([],'_'),Space([],'_'),Space([],'_')],[Space([],'_'),Space([],'*'),Space([],'_')],[Space([],'_'),Space([],'_'),Space([],'_')]] #middle board
b3 = [[Space([],'_'),Space([],'_'),Space([],'_')],[Space([],'_'),Space([],'*'),Space([],'_')],[Space([],'_'),Space([],'_'),Space([],'_')]] #outer board

print(b3[0][0].data+"     "+b3[0][1].data+"     "+b3[0][2].data+
    "\n  "+b2[0][0].data+"   "+b2[0][1].data+"   "+b2[0][2].data+
    "\n    "+b1[0][0].data+" "+b1[0][1].data+" "+b1[0][2].data+
    "\n"+b3[1][0].data+" "+b2[1][0].data+" "+b1[1][0].data+"   "+b3[1][2].data+" "+b2[1][2].data+" "+b1[1][2].data+
    "\n    "+b1[2][0].data+" "+b1[2][1].data+" "+b1[2][2].data+
    "\n  "+b2[2][0].data+"   "+b2[2][1].data+"   "+b2[2][2].data+
    "\n"+b3[2][0].data+"     "+b3[2][1].data+"     "+b3[2][2].data)

quit()