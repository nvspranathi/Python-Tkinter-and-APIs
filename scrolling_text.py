import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()

app_header = tk.Label(root,font=("Georgoia",24),text="Scrolled Text Demo")
app_header.pack()
text_scroll1 = scrolledtext.ScrolledText(root,wrap=tk.WORD,height=13,state=tk.DISABLED,bg='Light Grey')
text_scroll1.pack(fill=tk.BOTH,expand=True)
text_scroll1 = scrolledtext.ScrolledText(root,wrap=tk.WORD,height=3)
text_scroll1.pack(fill=tk.BOTH,expand=True)
root.mainloop()