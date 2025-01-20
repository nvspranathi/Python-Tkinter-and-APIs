from tkinter import scrolledtext
import tkinter as tk

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Cash Canvas")
        
        self.cci = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="WHITE", state=tk.DISABLED, height=30)
        self.cci.configure(state=tk.NORMAL)
        self.cci.insert(tk.END, "Hi there! I wish you first as always\n\n", "wish")
        self.cci.configure(state=tk.DISABLED)
        self.cci.pack(fill=tk.X, padx=10, pady=10)
        self.cci.tag_config("bot", foreground="GREEN", font=("Georgia", 12))
        self.cci.tag_config("wish", foreground="#008080", font=("Georgia", 16))  # Teal color, a mix of blue and green
        self.cci.tag_config("user", foreground="BLUE", font=("Georgia", 12))
        
        self.ms = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="LIGHT GREY", height=2)
        self.ms.pack(fill=tk.X, padx=10, pady=10)
        
        self.submit_button = tk.Button(root, text="SUBMIT", height=2, width=10, background="#4682B4", foreground="WHITE", command=self.on_click_submit)
        self.submit_button.pack(anchor=tk.W, padx=10)
    
    def on_click_submit(self):
        user_input = self.ms.get("1.0", tk.END)
        self.cci.configure(state=tk.NORMAL)
        self.cci.insert(tk.END, "\nYou said: " + user_input , "user")
        self.cci.insert(tk.END, "\nCanvas's reply: ", "bot")
        if "hi" in user_input.lower() or "hello" in user_input.lower():
            self.cci.insert(tk.END, "Hi there! How's your rupee doing today?\n", "bot")
        else:
            self.cci.insert(tk.END, "I think it's time to log today's budget—let's track your earnings, spending, and any transactions.\n", "bot")
        
        self.ms.delete("1.0", tk.END)
        self.cci.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatInterface(root)
    root.mainloop()