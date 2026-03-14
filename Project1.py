import tkinter as tk
window = tk.Tk()
window.title("CALCULATOR")
window.geometry("340x300")
entry = tk.Entry(window,width = 20,font = ("Calibiri",20), borderwidth = 5, justify = "right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))
def clear():
    entry.delete(0, tk.END)
def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)   
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]
for (text,row,col) in buttons:
    if text == "C":
        button = tk.Button(window, text=text, width=5, height=2, command=clear)
    elif text == "=":
        button = tk.Button(window, text=text, width=5, height=2, command=calculate)
    else:
        button = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: click(t))

    button.grid(row=row, column=col, padx=5, pady=5)
window.mainloop()

