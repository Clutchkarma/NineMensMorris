from hashlib import new
from mimetypes import init
from tkinter import *

class Game(Frame):

    def __init__(self) -> None:
        Frame.__init__(self)
        self.master.title("NineMen's Morris")
        self.grid()
        
        #create and draw board
        self.board = Canvas(self,width=300,height=300)
        self.board.grid(row=0,columnspan=2)
        
        #outer and inner shells
        self.board.create_polygon([12,12,12,290,290,290,290,12],fill="white",outline="black")
        self.board.create_polygon([50,50,50,250,250,250,250,50],fill="white",outline="black")
        
        #layer connecting lines
        self.board.create_line(12,150,290,150)
        self.board.create_line(150,12,150,290)

        #inner shell
        self.board.create_polygon([100,100,100,200,200,200,200,100],fill="white",outline="black")
        
        #inner shell spaces
        self.board.create_oval(90,90,110,110, fill='white')
        self.board.create_oval(140,90,160,110, fill='white')
        self.board.create_oval(190,90,210,110, fill='white')
        self.board.create_oval(90,190,110,210, fill='white')
        self.board.create_oval(140,190,160,210, fill='white')
        self.board.create_oval(190,190,210,210, fill='white')
        self.board.create_oval(90,140,110,160, fill='white')
        self.board.create_oval(190,140,210,160, fill='white')

        self.board.create_oval(90,90,110,110, fill='white')
        self.board.create_oval(140,90,160,110, fill='white')
        self.board.create_oval(190,90,210,110, fill='white')
        self.board.create_oval(90,190,110,210, fill='white')
        self.board.create_oval(140,190,160,210, fill='white')
        self.board.create_oval(190,190,210,210, fill='white')
        self.board.create_oval(90,140,110,160, fill='white')
        self.board.create_oval(190,140,210,160, fill='white')

        #middle shell spaces
        self.board.create_oval(40,40,60,60, fill='white')
        self.board.create_oval(140,40,160,60, fill='white')
        self.board.create_oval(240,40,260,60, fill='white')
        self.board.create_oval(40,240,60,260, fill='white')
        self.board.create_oval(140,240,160,260, fill='white')
        self.board.create_oval(240,240,260,260, fill='white')
        self.board.create_oval(40,140,60,160, fill='white')
        self.board.create_oval(240,140,260,160, fill='white')

        #outer shell spaces
        self.board.create_oval(2,2,22,22, fill='white')
        self.board.create_oval(140,2,160,22, fill='white')
        self.board.create_oval(280,2,300,22, fill='white')
        self.board.create_oval(2,280,22,300, fill='white')
        self.board.create_oval(140,280,160,300, fill='white')
        self.board.create_oval(280,280,300,300, fill='white')
        self.board.create_oval(2,140,22,160, fill='white')
        self.board.create_oval(280,140,300,160, fill='white')

        self.boardInfo = [[[([None,[0,0,1],[0,1,0],None],self.board.create_oval(5,5,19,19, fill='white',outline='white')),([[1,0,1],[0,0,2],None,[0,0,0]],'o'),([None,None,[0,0,1],[0,1,2]],'o')],
        [([[0,0,0],None,[0,2,0],[1,1,0]],'o'),([None,None,None,None],' '),([[0,0,2],[1,1,2],[0,2,2],None],'o')],
        [([[0,1,0],[0,2,1],None,None],'o'),([None,[0,2,2],[1,2,1],[0,2,0]],'o'),([[0,1,2],None,None,[0,2,1]],'o')]],
        [[([None,[1,0,1],[1,1,0],None],'o'),([[2,0,1],[1,0,2],[0,0,1],[1,0,0]],'o'),([None,None,[1,0,1],[1,1,2]],'o')],
        [([[1,0,0],[0,1,0],[1,2,0],[2,1,0]],'o'),([None,None,None,None],' '),([[1,0,2],[2,1,2],[1,2,2],[0,1,2]],'o')],
        [([[1,1,0],[1,2,1],None,None],'o'),([[0,2,1],[1,2,2],[2,2,1],[1,2,0]],'o'),([[1,1,2],None,None,[1,2,1]],'o')]],
        [[([None,[2,0,1],[2,1,0],None],'o'),([None,[2,0,2],[1,0,1],[2,0,0]],'o'),([None,None,[2,1,2],[2,0,1]],'o')],
        [([[2,0,0],[1,1,0],[2,2,0],None],'o'),([None,None,None,None],' '),([[2,0,2],None,[2,2,2],[1,1,2]],'o')],
        [([[2,1,0],[2,2,1],None,None],'o'),([[1,2,1],[2,2,2],None,[2,2,0]],'o'),([[2,1,2],None,None,[2,2,1]],'o')]]]

        #text output
        self.textOutput = StringVar()
        self.textOutput.set("Game Info")
        self.message = Label(self, textvariable = self.textOutput, font = "Courier 8")
        self.message.grid(row = 1,columnspan=3)

        # Prompt, Entry and Button
        self.prompt = Label(self, text = "Enter Layer: ")
        self.prompt.grid(row = 2, column = 0)
      
        self.z = Entry(self)
        self.z.grid(row = 2, column = 1)

        self.prompt = Label(self, text = "Enter y coordinate: ")
        self.prompt.grid(row = 3, column = 0)
      
        self.y = Entry(self)
        self.y.grid(row = 3, column = 1)

        self.prompt = Label(self, text = "Enter x coordinate: ")
        self.prompt.grid(row = 4, column = 0)
      
        self.x = Entry(self)
        self.x.grid(row = 4, column = 1)

        self.button_submit = Button( self, text = "Submit")
        self.button_submit.grid(row = 5, column = 1)

        


mainGame = Game()
mainGame.mainloop()
