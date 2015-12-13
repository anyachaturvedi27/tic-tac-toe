import Tkinter
import tkMessageBox
from Tkinter import *

count=0
cant = [[0 for r in range(3)]for c in range(3)]

for r in range(3):
    for c in range(3):
        cant[r][c]=0

flag=0
        
start=Tkinter.Tk()
start.title("Tic Tac Toe")
button_frame=Tkinter.Frame(start)
button_frame.pack(fill=Tkinter.X,side=Tkinter.BOTTOM)

def result(x):
  if x==1:
      result["text"]="Player 1 wins."
  elif x==2:
      result["text"]="Player 2 wins."
  else:
      result["text"]="No winner."

def change(x,y):
    global flag
    if cant[x][y]<1 and flag==0:
     global count
     count+=1
     cant[x][y]+=1
     if count%2==0:
        button[x][y]["text"] = "O"
     else:
        button[x][y]["text"] = "X"
     if count>4:
        for a in range(3):
          if button[a][0]["text"]==button[a][1]["text"] and button[a][1]["text"]==button[a][2]["text"]:
            if button[a][0]["text"]=="X":
              print "Player 1 wins."
              flag=1
            elif button[a][0]["text"]=="O":
              print "Player 2 wins."
              flag=1
          elif button[0][a]["text"]==button[1][a]["text"] and button[1][a]["text"]==button[2][a]["text"]:
            if button[0][a]["text"]=="X":
              print "Player 1 wins."
              flag=1
            elif button[0][a]["text"]=="O":
              print "Player 2 wins."
              flag=1
          elif button[0][0]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][2]["text"]:
            if button[0][0]["text"]=="X":
              print "Player 1 wins."
              flag=1
            elif button[0][0]["text"]=="O":
              print "Player 2 wins."
              flag=1
            break
          elif button[0][2]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][0]["text"]:
            if button[0][2]["text"]=="X":
              print "Player 1 wins."
              flag=1
            elif button[0][2]["text"]=="O":
              print "Player 2 wins."
              flag=1
            break
          elif count==9:
              print "No one wins."
              flag=1
              break
          elif flag==1:
              break
     
def play_again():
    global count
    for r in range(3):
       for c in range(3):
        button[r][c]["text"]=" "
        cant[r][c]=0
        count=0
    

def goodbye():
    start.destroy()


button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.rowconfigure(0,weight=1)
button_frame.rowconfigure(1,weight=1)
button_frame.rowconfigure(2,weight=1)

button = [[0 for r in range(3)]for c in range(3)]
button_number = 1
for r in range(3):
    for c in range(3):
        button[r][c]= Tkinter.Button(button_frame, text = button_number, command = lambda a=r,b=c:change(a,b))
        #button[r][c].grid(row=r, column=c, sticky="ew")
        button[r][c].grid(row=r,column=c,sticky=Tkinter.W+Tkinter.E)
        button_number += 1




playagain=Tkinter.Button(start,text="Play Again!",command = play_again)
playagain.pack()

C = Tkinter.Button(start, text="Quit", command = goodbye)
C.pack()

#result=Tkinter.Button(start,text="Result",command = result)
#result.pack()

start.mainloop()
