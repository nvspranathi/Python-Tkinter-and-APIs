# tk+inter=>toolkit interface
# built in library in py that helps you create GUI for your application

import tkinter # Tells the computer to allow user to use all the tools available in the tkinter library to create a graphical window
root  = tkinter.Tk() # root becomes main bg window or container. it got permission to place all tools from tkinter library.

name_label = tkinter.Label(root,text="Enter your Name")
name_label.pack()
name_textbox = tkinter.Entry(root)
name_textbox.pack() # pack organises

email_label = tkinter.Label(root,text="Enter your Email")
email_label.pack()
email_textbox = tkinter.Entry(root)
email_textbox.pack() # pack organises

root.mainloop() # window stays alive(loop).






'''print((root))
class Hai:
    def __init__(self):
        pass
    def nothing(self):
        print("nothing")

print(Hai,type(Hai))
print(Hai(),type(Hai()))'''