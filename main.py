from tkinter import *
version = "1.0.0"

root = Tk()
root.title(f"완전 멋진 가림판")
root.geometry("400x500-500+140")
root.iconbitmap('icon.ico')
root.wm_attributes("-topmost", 1)
root.mainloop()