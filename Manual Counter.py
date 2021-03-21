import time
from tkinter import *

root = Tk()

#Size of Window and Background Color
root.geometry("122x115+1600+10")
root.resizable(False,False)
root.configure(background="black")

#Hide Window Frame
root.overrideredirect(1)

#Variables for Window: 
# p - units digit 
# s - dozens digit
# res - start the counting if = 0

p=-1
s=0
res=0

#Function to get 1 unit in p variable if res = 0
def click():
    global p,s,res
    if res==0:
        p=p+1
        if p==10:
            p=0
            s=s+1
    else:
        p=0
        s=0
        res=0

    label1=Label(root,font=("alarm clock",60,"bold"),text='%i%i'%(s,p), bd=0,bg='black', fg="red", padx=0, pady=0)
    label1.grid(row=2,column=1, columnspan=2, ipadx=15, ipady=4)

#Function to reset digits to 0 by res = 1
def rs():
    global res
    res=1
    click()

button1=Button(root,text="Click",command=click, width=7,borderwidth=2)
button1.grid(row=1,column=1,sticky='W',pady=0)
button2=Button(root,text="Reset",command=rs, width=7,borderwidth=2)
button2.grid(row=1,column=2,sticky='W')

click()
root.mainloop()