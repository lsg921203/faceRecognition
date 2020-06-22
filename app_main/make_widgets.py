import tkinter as tk

def make(app):
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.bnt1 = tk.Button(app.sub_fr, width=10, font=60, text="btn1")
    app.bnt2 = tk.Button(app.sub_fr, width=10, font=60, text="btn2")
    app.bnt3 = tk.Button(app.sub_fr, width=10, font=60, text="btn3")

    app.ent.grid(row=0, column=0, columnspan=3)
    app.bnt1.grid(row=1, column=0)
    app.bnt2.grid(row=1, column=1)
    app.bnt3.grid(row=1, column=2)