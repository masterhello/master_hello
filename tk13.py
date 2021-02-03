#tk13.pyw
import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
lb = tk.Label(text='This is a label, This is a label, this is a label')
ms = tk.Message(text='This is a Messege. This is a Message. This is a Messege')
[widget.pack() for widget in (lb,ms)]

root.mainloop()