import random as rd
from tkinter import *
from tkinter import ttk

w=400
h=400
class snake():
    def __init__(self):
        self.x=5
        self.y=5
        self.coordx=[]
        self.coordy=[]
        self.coordx.append(self.x)
        self.coordy.append(self.y)
        self.length=1
        self.opposet={'Right':'Left','Down':'Up','Left':'Right','Up':'Down'}
        self.lastkey='Right'

    def reset(self):
        self.__init__()

    def getsnakex(self) :
        return self.coordx
    def getsnakey(self) : 
        return self.coordy
    def getLastKey(self):
         return self.lastkey
        
           
    def collision (self):
        for i in range(1,self.length, 1):
            if self.coordy[0] == self.coordy[i] and self.coordx[0] == self.coordx[i]:
                return True
               # snake ate itself
        if self.coordx[0] < 1 or self.coordx[0] >= w - 1 or self.coordy[0] < 1 or self.coordy[0] >= h- 1:
                return True
              # snake out of bounds return False
        self.eat()
    

    def direction (self,e ):
        for i in range(self.length-1,0,-1):
            self.coordx[i] = self.coordx[i - 1]
            self.coordy[i] = self.coordy[i - 1]
        if e == 'Right':
                self.coordx[0]+=5
        if e == 'Left':
                self.coordx[0]-=5
        if e == 'Up':
               self.coordy[0]-=5
        if e == 'Down':
               self.coordy[0]+=5


    def user_won(self):
        if self.length -1 == 10000:
            return True       
        

    def currentdirec(self,event):
        if event.keysym != self.lastkey and self.lastkey != self.opposet[event.keysym]:
            self.lastkey=event.keysym
        print(self.lastkey)

    def eat(self):
        if self.coordx[0]==f.getfoodx() and self.coordy[0]==f.getfoody():
            # snake grows
            self.length+=1
            x = self.coordx[len(self.coordx) - 1] 
            y = self.coordy[len(self.coordy) - 1]
            if self.lastkey=='Right' or self.lastkey=="Left" :
                self.coordx.append(x -5)
                self.coordy.append(y)
            else :
                self.coordx.append(x )
                self.coordy.append(y-5)
                
            f.createnewfood()



class food():
    x=22
    y=22
    def __init__(self): 
        while(self.x % 5 !=0):
            self.x = rd.randint(1, w - 1) 
        while(self.y % 5 !=0):
            self.y = rd.randint(1, h - 1) 

    def reset(self):
        self.__init__()

    def getfoodx(self)-> int : 
        return self.x

    def getfoody(self)-> int: 
        return self.y
        
    def createnewfood(self): 
        self.x=22
        self.y=22
        while(self.x % 5 !=0):
            self.x = rd.randint(1, w - 1) 
        while(self.y % 5 !=0):
            self.y = rd.randint(1, h - 1) 



class GameLoop():
    def paint(self):
        c.after(200,self.paint)
        c.delete(ALL)
        if not s.collision() and not s.user_won():
            x=s.getsnakex()
            y=s.getsnakey()
            for i in range (0,s.length):
                c.create_oval(x[i],y[i] ,x[i]+10 ,y[i]+10, fill="red") #snake 
                c.create_oval(f.getfoodx(),f.getfoody(),f.getfoodx()+10,f.getfoody()+10,fill="green") #food
            espace.bind("<KeyPress-Left>" ,lambda event :s.currentdirec(event))
            espace.bind("<KeyPress-Right>",lambda event :s.currentdirec(event))
            espace.bind("<KeyPress-Up>"   ,lambda event :s.currentdirec(event))
            espace.bind("<KeyPress-Down>" ,lambda event :s.currentdirec(event))
            s.direction(s.getLastKey())
        else :
            c.create_text(w  / 2, h / 2 , fill="darkblue", font="Times 20 italic bold", text="GameOver!")
            c.create_text(w  / 2+5, h / 2 +20 , fill="darkblue", font="Times 20 italic bold", text="votre score : "+str(s.length-1))
            b1.place(x=140,y=250)
            b2.place(x=210,y=250)
            if s.user_won():
                l2.place(x=40,y=100)





    def play_again(self):
        if (s.user_won()):
            l2.place_forget()
        c.pack_forget()
        s.reset()
        f.reset()
        b1.place_forget()
        b2.place_forget()
        c.pack()

    def leave(self):
        l.place(x=105,y=100)
        espace.after(500,espace.destroy)


s=snake()
f=food()
espace =Tk()
c = Canvas(espace,width=w,height=w,bg="black")
c.pack()
gameLoop = GameLoop()
gameLoop.paint()
l=Label( font=("Times 20 italic bold",50), text="loser!")
l2=Label( font=("Times 20 italic bold",50), text=" You Won !")
b1=Button(text="Try again ",bg="blue",command=lambda:gameLoop.play_again())
b2=Button(text="Exit ",bg="red",command=lambda:gameLoop.leave())
espace.resizable(False, False)
mainloop()
