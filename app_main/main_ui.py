import cv2
import tkinter as tk
import numpy as np
from PIL import Image
from PIL import ImageTk


class AppWindow(tk.Frame): #frame
    def __init__(self,master=None, size=None, path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame을 띄울거임
        self.sub_fr = None#하위 프레임
        self.src = None
        self.frame = None # tk의 label에 출력한 영상
        self.create_widgets(path)

    def make_img(self, path):
        src = cv2.imread(path)
        src = cv2.resize(src, (640, 400))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)# 색상변환은 이걸로
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)


    def create_widgets(self, path):
        self.make_img(path)
        self.frame = tk.Label(self.master, image=self.src)
        self.frame.pack()
        self.sub_fr = tk.Frame(self.master)
        self.sub_fr.pack()

    def change_img(self, res):
        res = cv2.resize(res, (640,400))
        img = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.frame['image'] = self.src