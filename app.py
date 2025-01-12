import tkinter as tk
from tkinter import PhotoImage
# from PIL import Image,ImageTk

root = tk.Tk()
root.title("My app")
root.geometry("500x400")
# image = Image.open(r"photo.png")
# image_path = ImageTk.PhotoImage(image)
image_path = PhotoImage(file="photo.png")
bg_image = tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)
text_label = tk.Label(root,text="Welcome to my app",font=("Georgia",24))
text_label.pack()

root.mainloop()
