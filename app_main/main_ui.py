import cv2
import tkinter as tk
class AppWindow(tk.Frame):
    def __init__(self,master=None, size=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()
        self.sub_fr = tk.Frame()
        self.sub_fr.pack()
        self.src = None
        self.create_widgets()

    def create_widgets(self, ):
        print("")
