import time
from tkinter import *

root = Tk()

#Size of Window and Background Color
root.geometry("343x77+1400+10")
root.configure(background="black")
root.resizable(0,0)

#Hide Window Frame
root.overrideredirect(1)

#Function to get Live Time
def start():
    text=time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(1,start)

label=Label(root,font=("alarm clock",60,"bold"),bg='black',fg="red",bd=0, height=1, padx=6, pady=0)
label.grid(row=1,column=0, columnspan=20)

start()
root.mainloop()