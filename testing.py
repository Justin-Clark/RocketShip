#!/usr/bin/env python3

import tkinter
import tkinter.ttk

root = tkinter.Tk()

style_base = tkinter.ttk.Style()
style_base.configure("BW.TLabel", foreground="black", background="white")

label_1 = tkinter.ttk.Label(text="TestLABEL", style="BW.TLabel")
label_1.pack()

root.title("TK BASE")
root.geometry("500x500")

root.mainloop()
