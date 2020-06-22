
import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw

def main():
    img_path = "img/sparrow.jpg"
    root = tk.Tk()
    app = win.AppWindow(root, "650x500+100+100",img_path)
    mkw.make(app=app)
    app.mainloop()