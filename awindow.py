from typing import List, Optional
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass

root = Tk()
root.geometry("800x600")
root.title("Daddy chill")

# do menu things
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

# do mainframe things
mainframe = ttk.Frame(root, padding=(10, 10, 10, 10))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# a functional widget built in the mainframe
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# a label widget that uses a variable (updated by func defined above)
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# a button widget
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# more label widgets
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()