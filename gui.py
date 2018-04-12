import tkinter as tk
from tkinter import simpledialog

def enterHandler(e=None):
    input = entry.get()
    print(input)
    messages.insert(tk.INSERT, input + '\n')
    entry.delete(0, tk.END)

root = tk.Tk()

namePrompt = tk.simpledialog.askstring('Test', 'Enter your name')
print(namePrompt)

userInput = tk.StringVar()
entry = tk.Entry(root, text=userInput)
messages = tk.Text(root)
sendBtn = tk.Button(root, text='Send', command=enterHandler)

entry.bind('<Return>', enterHandler) # enter
sendBtn.pack()
messages.pack()
entry.pack(side=tk.BOTTOM, fill=tk.X)
root.mainloop()
