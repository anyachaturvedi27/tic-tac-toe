#hello
import Tkinter
import tkMessageBox
from Tkinter import *
import random
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
      print "Computer wins."
  elif x==2:
      print "Player wins."
  else:
      print "No winner."

def change(x,y):
    global flag
    t=0
    if cant[x][y]<1 and flag==0:
     global count
     count+=1
     cant[x][y]+=1
     i=random.randint(0,2)
     j=random.randint(0,2)
     button[x][y]["text"] = "O"
     if count==1:
        if cant[1][1]==0:
            button[1][1]["text"]="X"
            cant[1][1]+=1
            t=1
     if count>2:
        for a in range(3):
          if button[a][0]["text"]==button[a][1]["text"] and button[a][1]["text"]==button[a][2]["text"] and flag==0:
            if button[a][0]["text"]=="X":
              print "Computer wins."
              flag=1
              
            elif button[a][0]["text"]=="O":
              print "Player wins."
              flag=1
              
          elif button[0][a]["text"]==button[1][a]["text"] and button[1][a]["text"]==button[2][a]["text"] and flag==0:
            if button[0][a]["text"]=="X":
              print "Computer wins."
              flag=1
              
            elif button[0][a]["text"]=="O":
              print "Player wins."
              flag=1
              
        if button[0][0]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][2]["text"] and flag==0:
            if button[0][0]["text"]=="X":
              print "Computer wins."
              flag=1
            
            elif button[0][0]["text"]=="O":
              print "Player wins."
              flag=1
              
        elif button[0][2]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][0]["text"] and flag==0:
            if button[0][2]["text"]=="X":
              print "Computer wins."
              flag=1
             
            elif button[0][2]["text"]=="O":
              print "Player wins."
              flag=1
              
        elif count==5 and flag==0:
              print "It's a draw."
              flag=1
             

    
     if count>=2 and flag==0:
       for a in range(3):
          if t==0:
           if button[a][0]["text"]==button[a][1]["text"]=="X" or button[a][1]["text"]==button[a][2]["text"]=="X" or button[a][0]["text"]==button[a][2]["text"]=="X":
              for k in range(3):
                if cant[a][k]==0:
                    button[a][k]["text"]="X"
                    cant[a][k]+=1
                    t=1
                    break
           elif button[0][a]["text"]==button[1][a]["text"]=="X" or button[1][a]["text"]==button[2][a]["text"]=="X" or button[0][a]["text"]==button[2][a]["text"]=="X" :
            for k in range(3):
                if cant[k][a]==0:
                    button[k][a]["text"]="X"
                    cant[k][a]+=1
                    t=1
                    break
       if t==0:
           if button[0][0]["text"]==button[1][1]["text"]=="X" or button[1][1]["text"]==button[2][2]["text"]=="X" or button[0][0]["text"]==button[2][2]["text"]=="X":
            for k in range(3):
                if cant[k][k]==0:
                    button[k][k]["text"]="X"
                    cant[k][k]+=1
                    t=1
                    break
       if t==0:
         if button[0][2]["text"]==button[1][1]["text"]=="X" or button[1][1]["text"]==button[2][0]["text"]=="X" or button[0][2]["text"]==button[2][0]["text"]=="X" :
            if cant[0][2]==0:
               button[0][2]["text"]="X"
               cant[0][2]+=1
               t=1
            
            elif cant[1][1]==0:
               button[1][1]["text"]="X"
               cant[1][1]+=1
               t=1
            elif cant[2][0]==0:
               button[2][0]["text"]="X"
               cant[2][0]+=1
               t=1   
       for a in range(3):
          if t==0:
           if button[a][0]["text"]==button[a][1]["text"]=="O" or button[a][1]["text"]==button[a][2]["text"]=="O" or button[a][0]["text"]==button[a][2]["text"]=="O":
              for k in range(3):
                if cant[a][k]==0:
                    button[a][k]["text"]="X"
                    cant[a][k]+=1
                    t=1
                    break
           elif button[0][a]["text"]==button[1][a]["text"]=="O" or button[1][a]["text"]==button[2][a]["text"]=="O" or button[0][a]["text"]==button[2][a]["text"]=="O" :
            for k in range(3):
                if cant[k][a]==0:
                    button[k][a]["text"]="X"
                    cant[k][a]+=1
                    t=1
                    break
       if t==0:
           if button[0][0]["text"]==button[1][1]["text"]=="O" or button[1][1]["text"]==button[2][2]["text"]=="O" or button[0][0]["text"]==button[2][2]["text"]=="O":
            for k in range(3):
                if cant[k][k]==0:
                    button[k][k]["text"]="X"
                    cant[k][k]+=1
                    t=1
                    break
       if t==0:
           if button[0][2]["text"]==button[1][1]["text"]=="O" or button[1][1]["text"]==button[2][0]["text"]=="O" or button[0][2]["text"]==button[2][0]["text"]=="O" :
            if cant[0][2]==0:
               button[0][2]["text"]="X"
               cant[0][2]+=1
               t=1
            
            elif cant[1][1]==0:
               button[1][1]["text"]="X"
               cant[1][1]+=1
               t=1
            elif cant[2][0]==0:
               button[2][0]["text"]="X"
               cant[2][0]+=1
               t=1
          
     if x==i and y==j and t==0 and flag==0:
        if x==0 and y==0:
          if cant[1][1]==0:
            button[1][1]["text"]="X"
            cant[1][1]+=1
          else:
            for s in range(3):
               for t in range(3):
                 if cant[s][t]==0:
                     button[s][t]["text"]="X"
                     cant[s][t]+=1
                     break
               break
                   
        elif x==2 and y==2:
          if x==0 and y==0:
           if cant[1][1]==0:
            button[1][1]["text"]="X"
            cant[1][1]+=1
          else:
            for s in range(3):
               for t in range(3):
                 if cant[s][t]==0:
                     button[s][t]["text"]="X"
                     cant[s][t]+=1
                     break
               break
        else:
            if cant[i-1][j-1]==0:
             button[i-1][j-1]["text"]="X"
             cant[i-1][j-1]+=1
            else:
             for s in range(3):
               for t in range(3):
                 if cant[s][t]==0:
                     button[s][t]["text"]="X"
                     cant[s][t]+=1
                     break
               break
            
     elif t==0 and flag==0:
        if cant[i][j]==0:
            button[i][j]["text"]="X"
            cant[i][j]+=1
        else:
             for s in range(3):
               for t in range(3):
                 if cant[s][t]==0:
                     button[s][t]["text"]="X"
                     cant[s][t]+=1
                     break
               break
        
     if count>2 and flag==0:
        for a in range(3):
          if button[a][0]["text"]==button[a][1]["text"] and button[a][1]["text"]==button[a][2]["text"] and flag==0:
            if button[a][0]["text"]=="X":
              print "Computer wins."
              flag=1
             
            elif button[a][0]["text"]=="O":
              print "Player wins."
              flag=1
              
          elif button[0][a]["text"]==button[1][a]["text"] and button[1][a]["text"]==button[2][a]["text"] and flag==0:
            if button[0][a]["text"]=="X":
              print "Computer wins."
              flag=1
              
            elif button[0][a]["text"]=="O":
              print "Player wins."
              flag=1
              
        if button[0][0]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][2]["text"] and flag==0:
            if button[0][0]["text"]=="X":
              print "Computer wins."
              flag=1
              
            elif button[0][0]["text"]=="O":
              print "Player wins."
              flag=1
              
        elif button[0][2]["text"]==button[1][1]["text"] and button[1][1]["text"]==button[2][0]["text"] and flag==0:
            if button[0][2]["text"]=="X":
              print "Computer wins."
              flag=1
              
            elif button[0][2]["text"]=="O":
              print "Player wins."
              flag=1
              
        elif count==5 and flag==0:
              print "It's a draw."
              flag=1
              
        
def goodbye():
    start.destroy()


 #result=Tkinter.Button(start,text="Result",command = result)
 #result.pack()

       
    




button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.rowconfigure(0,weight=1)
button_frame.rowconfigure(1,weight=1)
button_frame.rowconfigure(2,weight=1)

button = [[0 for r in range(3)]for c in range(3)]
button_number = 1
for r in range(3):
    for c in range(3):
        button[r][c]= Tkinter.Button(button_frame, text = " ", command = lambda a=r,b=c:change(a,b))
        #button[r][c].grid(row=r, column=c, sticky="ew")
        button[r][c].grid(row=r,column=c,sticky=Tkinter.W+Tkinter.E)
        button_number += 1






C = Tkinter.Button(start, text="Quit", command = goodbye)
C.pack()

#result=Tkinter.Button(start,text="Result",command = result)
#result.pack()

start.mainloop()

#switched to new branch play-again
