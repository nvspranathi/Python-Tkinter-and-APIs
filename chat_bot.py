import tkinter as tk
from tkinter import scrolledtext,messagebox

# function to be called when the submit button is clicked
def OnClick_Submit():
    UserInput = user_space.get("1.0",tk.END)
    bot_screen.configure(state=tk.NORMAL)
    bot_screen.insert(tk.END,"\nUser: "+UserInput)
    user_space.delete("1.0",tk.END)
    bot_screen.configure(state=tk.DISABLED)

# main window
root = tk.Tk()

# heading for the window or the interface
app_header = tk.Label(root,text="MY CHAT BOT",font=("Georgia",20))
app_header.pack(fill=tk.BOTH,expand=True)

# scrolled text for the bot
bot_screen = scrolledtext.ScrolledText(root,wrap=tk.WORD,bg="WHITE",state=tk.DISABLED,height=30)
bot_screen.pack(fill=tk.BOTH,expand=True)

# scrolled text for the user
user_space = scrolledtext.ScrolledText(root,wrap=tk.WORD,bg="LIGHT GREY",height=2)
user_space.pack(fill=tk.BOTH,expand=True)

# submit button
submit_button = tk.Button(root,text="Submit",height=2,width=10,command=OnClick_Submit)
submit_button.pack(anchor=tk.W,padx=10)

# main loop
root.mainloop()