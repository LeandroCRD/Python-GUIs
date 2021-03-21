from tkinter import *
from yahoo_fin import stock_info as si
import time

root = Tk()

#Size of Window and Background Color
root.geometry("279x140+1642+0")
root.configure(background="black")
root.resizable(0,0)

#Hide Window Frame
root.overrideredirect(1)

#Variables for Window: 
# y - old price 
# x1 - recent price
# money - $ invested 
# perc - % change btw y and x1

y = float(0)
x1 = 0
money = 1000
perc = 0

#Function to get Live Price of Stock + Store Value in Variables
def visio():
    global count, x, y, x1, money
    stock1 = si.get_live_price("TSLA")
    x = float("%.2f" % stock1)
    x1 = float(stock1)
    money = 1.53846 * stock1
    perc = round((((stock1 - 650) / 650)*100),2)
    print("%.2f" % stock1)
    
    #Conditional to Print in Window Stock Price in Green or Red Color
    if y > x:
        label=Label(root,font=("alarm clock",60,"bold"),text="%.2f" % x,bg='black',fg="red",bd=0, height=1, padx=10, pady=0)
        label.grid(row=1,column=0, columnspan=2)
        label=Label(root,font=("alarm clock",8,"bold"),text="TESLA   ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=2,column=1, sticky = E, padx=10)
        label=Label(root,font=("alarm clock",8,"bold"),text="+" + "%.2f" % perc + "   ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=3,column=1, sticky = E, padx=10, pady = 5)
        label=Label(root,font=("alarm clock",8,"bold"),text=("%.2f" % money) + "  ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=4,column=1, sticky = E, padx=13, pady=2)
        label.after(2000,visio)
    else:
        label=Label(root,font=("alarm clock",60,"bold"),text="%.2f" % x,bg='black',fg="green",bd=0, height=1, padx=10, pady=0)
        label.grid(row=1,column=0, columnspan=2)
        label=Label(root,font=("alarm clock",8,"bold"),text="TESLA   ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=2,column=1, sticky = E, padx=10)
        label=Label(root,font=("alarm clock",8,"bold"),text="" + "%.2f" % perc + "   ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=3,column=1, sticky = E, padx=10, pady = 5)
        label=Label(root,font=("alarm clock",8,"bold"),text=("%.2f" % money) + "   ",bg='black',fg="green",bd=0, height=1, padx=0, pady=0)
        label.grid(row=4,column=1, sticky = E, padx=13, pady=2)
        label.after(2000,visio)
    
    y = x1

visio()
root.mainloop()