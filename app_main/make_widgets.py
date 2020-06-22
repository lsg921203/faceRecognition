import tkinter as tk
from functools import partial

def btn1_clicked(app, service, event):
    print (event)
    flag = service.face_detect()
    if flag:
        pass
def btn2_clicked():
    print ("btn2_clicked")

def btn3_clicked():
    print ("btn3_clicked")

def make(app, service):# 버튼을 수정하기 위해서
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.bnt1 = tk.Button(app.sub_fr, width=10, font=60, text="얼굴인식")
    app.bnt2 = tk.Button(app.sub_fr, width=10, font=60, text="눈인식")
    app.bnt3 = tk.Button(app.sub_fr, width=10, font=60, text="미소인식")

    app.ent.grid(row=0, column=0, columnspan=3)
    app.bnt1.grid(row=1, column=0)
    app.bnt2.grid(row=1, column=1)
    app.bnt3.grid(row=1, column=2)

    #app.bnt1['command'] = btn1_clicked
    app.bnt1.bind('<Button-1>',partial(btn1_clicked, app, service))
    app.bnt2['command'] = btn2_clicked
    app.bnt3['command'] = btn3_clicked