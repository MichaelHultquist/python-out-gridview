#######
# Name: outGridviewPy.py
# Author: Michael Hultquist
# Date: 12/11/2025
# Purpose: To create a visual grid of data from Python arrays for confirmation and development purposes.
#
########

import tkinter as tk
from tkinter import ttk

def outGridview(inputArray,columnsArray,title):

    gridViewTitle = title

    root = tk.Tk()
    root.title(gridViewTitle)

    tree = ttk.Treeview(root, columns=columnsArray, show='headings')

    for cols in columnsArray:
        tree.column(cols)
        tree.heading(cols, text=cols)

    hsb = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
    vsb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)

    hsb.pack(side='bottom', fill='x')
    vsb.pack(side='right', fill='y')

    tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

    for input in inputArray:
        dictionaries = []
        for item in input:
            dictionaries.append(item)
            print(dictionaries)
        tree.insert('',tk.END,values=(dictionaries))

    tree.pack(expand=True, fill='both')
    root.mainloop()