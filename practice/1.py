import Tkinter
import tkMessageBox

top = Tkinter.Tk()
top.title("1")

def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

def goodbye():
    top.destroy()

def changetext():
    if D["text"] == "X":
        D["text"] = "O"
    else:
        D["text"] = "X"

        
        
B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()

C = Tkinter.Button(top, text="Goodbye", command = goodbye)
C.pack(side='bottom',padx=100,pady=5)

D= Tkinter.Button(top, text="X",command = changetext)
D.pack(side='bottom',padx=15,pady=10)

top.mainloop()
