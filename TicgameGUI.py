from tkinter import *
import tkinter.messagebox
class TicGameGui:
    def __init__(self):
        self.win = False
        self.x = 0
        self.o = 0
        self.answer = 0
        self.xarry = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.oarry = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.choosen = []
        self.player = " "
        window = Tk()
        window.title("Tic Game design by herbert")
        self.xImage = PhotoImage(file='x.png')
        self.oImage = PhotoImage(file='o.png')
        self.blankImage = PhotoImage(file='blank.png')
        frameU = Frame(window)
        frameU.pack()
        self.lbVar = StringVar()
        self.lbVar.set('begain Please X Player choose :')
        Label(frameU, textvariable=self.lbVar).grid(row=1, column=1)
        frameM = Frame(window)
        frameM.pack()
        self.bt0 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(0, 0))
        self.bt1 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(0, 1))
        self.bt2 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(0, 2))
        self.bt3 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(1, 0))
        self.bt4 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(1, 1))
        self.bt5 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(1, 2))
        self.bt6 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(2, 0))
        self.bt7 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(2, 1))
        self.bt8 = Button(frameM, image=self.blankImage, command=lambda: self.changeP(2, 2))
        self.bt0.grid(row=1, column=1)
        self.bt1.grid(row=1, column=2)
        self.bt2.grid(row=1, column=3)
        self.bt3.grid(row=2, column=1)
        self.bt4.grid(row=2, column=2)
        self.bt5.grid(row=2, column=3)
        self.bt6.grid(row=3, column=1)
        self.bt7.grid(row=3, column=2)
        self.bt8.grid(row=3, column=3)
        frameD = Frame(window)
        frameD.pack()
        Button(frameD, text='REFRESH', command=self.refresh).grid(row=2, column=2)
        window.mainloop()

    def changeP(self, x, y):
        if self.win != True:
            if [x, y] in self.choosen:
                self.lbVar.set('This block already choosen,please ' + self.player + ' choose:')

            else:
                self.choosen.append([x,y])
                    # x玩家输入并判断是否获胜
                if self.x <= self.o and self.x < 5:
                    self.player = "X"

                    self.lbVar.set('Please X Player choose :')
                    if x == 0 and y == 0:
                        self.bt0["image"] = self.xImage
                    elif x == 0 and y == 1:
                        self.bt1['image'] = self.xImage
                    elif x == 0 and y == 2:
                        self.bt2['image'] = self.xImage
                    elif x == 1 and y == 0:
                        self.bt3['image'] = self.xImage
                    elif x == 1 and y == 1:
                        self.bt4['image'] = self.xImage
                    elif x == 1 and y == 2:
                        self.bt5['image'] = self.xImage
                    elif x == 2 and y == 0:
                        self.bt6['image'] = self.xImage
                    elif x == 2 and y == 1:
                        self.bt7['image'] = self.xImage
                    elif x == 2 and y == 2:
                        self.bt8['image'] = self.xImage
                    self.xarry[x][y] = 1
                    self.x += 1
                    if self.x >= 2:
                        self.iswin(self.player)
                    if self.win != True:
                        self.lbVar.set('Please O Player choose :')
                        self.player = "O"
                elif self.o < 4:
                    self.player = "O"
                    self.lbVar.set('Please O Player choose :')
                    if x == 0 and y == 0:
                        self.bt0['image'] = self.oImage
                    elif x == 0 and y == 1:
                        self.bt1['image'] = self.oImage
                    elif x == 0 and y == 2:
                        self.bt2['image'] =self.oImage
                    elif x == 1 and y == 0:
                        self.bt3['image'] = self.oImage
                    elif x == 1 and y == 1:
                        self.bt4['image'] = self.oImage
                    elif x == 1 and y == 2:
                        self.bt5['image'] = self.oImage
                    elif x == 2 and y == 0:
                        self.bt6['image'] = self.oImage
                    elif x == 2 and y == 1:
                        self.bt7['image'] = self.oImage
                    elif x == 2 and y == 2:
                        self.bt8['image'] = self.oImage
                    self.oarry[x][y] = 1
                    self.o += 1
                    if self.o >= 2:
                        self.iswin(self.player)
                    if self.win != True:
                        self.lbVar.set('Please X Player choose :')
                        self.player = "X"
                    # o玩家输入并判断是否获胜


            if self.win and self.x != 5:
                self.lbVar.set('Congratulation '+self.player+' Player won!')
            elif self.win and self.x ==5:
                self.lbVar.set('Game is Draw')
                print("Game is Draw")

    def iswin(self, player):
        self.player = player
        if self.player == "X":
            array = self.xarry
        else:
            array = self.oarry
        #判断横向
        if self.answer != 3:
            for i in range(len(array)):
                self.answer = sum(array[i])
                if self.answer == 3:
                    self.win = True
                    break
        #判断纵向
        if self.answer != 3:
            for j in range(len(array[0])):
                self.answer = 0
                for i in range(len(array)):
                    self.answer += array[i][j]
                if self.answer == 3:
                    self.win = True
                    break
        #判断对角线
        if self.answer != 3:
            if array[0][0] + array[1][1] + array[2][2] == 3:
                #self.answer = array[0][0] + array[1][1] + array[2][2]
                self.win = True
        if self.answer != 3:
            if array[0][2] + array[1][1] + array[2][0] == 3:
                #self.answer = array[0][2] + array[1][1] + array[2][0]
                self.win = True
        if self.win != True and self.x == 5:
            self.win =True




    def refresh(self):
        self.lbVar.set('Begin Please X Player choose :')
        self.bt0['image'] = self.blankImage
        self.bt1['image'] = self.blankImage
        self.bt2['image'] = self.blankImage
        self.bt3['image'] = self.blankImage
        self.bt4['image'] = self.blankImage
        self.bt5['image'] = self.blankImage
        self.bt6['image'] = self.blankImage
        self.bt7['image'] = self.blankImage
        self.bt8['image'] = self.blankImage
        self.win = False
        self.x = 0
        self.o = 0
        self.answer = 0
        self.xarry = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.oarry = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.choosen = []
        self.player = " "









