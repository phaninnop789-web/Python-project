import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Learning tk")
window.geometry('400x300')
def click_me():
    input = entry.get()
    print("input is: "+ input)


label = tk.Label(text="My first label",)
label.pack()
entry = tk.Entry(window)
entry.pack()
def button_clicked():
    print("Button was clicked!")
button = ttk.Button(window,text="Click Me",command=button_clicked,)
button.pack(padx = 20,pady=20)
label2 = tk.Label(text="Username:")
label2.pack()
username = ttk.Entry(window)
username.pack()
window.mainloop()


