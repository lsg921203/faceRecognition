import tkinter as tk
from functools import partial

def btn1_clicked(app, service, event):
    print (event)
    flag = service.face_detect()
    if flag:
        app.change_img(service.res)
def btn2_clicked(app, service, event):
    print(event)
    flag = service.eye_detect()
    if flag:
        app.change_img(service.res)

def btn3_clicked(app, service, event):
    print(event)
    flag = service.smile_detect()
    if flag:
        app.change_img(service.res)

def btn4_clicked(service, event):
    print(event)
    service.face_recog_train()

def btn5_clicked(app, service, event):
    print(event)
    flag,name = service.face_recog()
    app.ent.delete(0,'end')
    #print(name)
    app.ent.insert(0,name)

def make(app, service):# 버튼을 수정하기 위해서
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.bnt1 = tk.Button(app.sub_fr, width=10, font=60, text="얼굴인식")
    app.bnt2 = tk.Button(app.sub_fr, width=10, font=60, text="눈인식")
    app.bnt3 = tk.Button(app.sub_fr, width=10, font=60, text="미소인식")
    app.bnt4 = tk.Button(app.sub_fr, width=10, font=60, text="얼굴학습")
    app.bnt5 = tk.Button(app.sub_fr, width=10, font=60, text="얼굴인식")

    app.ent.grid(row=0, column=0, columnspan=5)
    app.bnt1.grid(row=1, column=0)
    app.bnt2.grid(row=1, column=1)
    app.bnt3.grid(row=1, column=2)
    app.bnt4.grid(row=1, column=3)
    app.bnt5.grid(row=1, column=4)

    #app.bnt1['command'] = btn1_clicked
    app.bnt1.bind('<Button-1>',partial(btn1_clicked, app, service))
    app.bnt2.bind('<Button-1>',partial(btn2_clicked, app, service))
    app.bnt3.bind('<Button-1>',partial(btn3_clicked, app, service))
    app.bnt4.bind('<Button-1>', partial(btn4_clicked, service))
    app.bnt5.bind('<Button-1>', partial(btn5_clicked, app, service))