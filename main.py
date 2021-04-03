#calc
from tkinter import *


screen = Tk()
screen.geometry("400x450")
screen.title("Calc")
screenLabel = Label(screen, text = "calc",bg="dark gray",font=("times",30,"bold"))
screenLabel.pack(side=TOP)
screen.config(background="dark grey")

textin = StringVar()
operator = ""

def clickbut(number):   #lambda:clickbut(1)
        global operator
        operator = operator + str(number)
        textin.set(operator)

def equalbut():
        global operator
        add=str(eval(operator))
        textin.set(add)
        operator=""

def equalbut():
        global operator
        sub=str(eval(operator))
        textin.set(sub)
        operator=""

def equalbut():
        global operator
        mul=str(eval(operator))
        textin.set(mul)
        operator=""

def equalbut():
        global operator
        div=str(eval(operator))
        textin.set(div)
        operator=""

def clrbut():
    textin.set("")

    screentext=Entry(screen,font=("Courier New",12),textvar=textin, width=25,bd=5,bg="powder blue")
    screentext.pack()

    but1 = Button(screen,padx=14,pady=14,bd=4,bg="white",command=lambda: clickbut(1),text="1",font=("courier new",16))
    but1.place(x=10,y=100)
    but2 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(2), text="2",font=("courier new", 16))
    but2.place(x=10, y=170)
    but3 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(3), text="3",font=("courier new", 16))
    but3.place(x=10, y=240)
    but4 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(4), text="4",font=("courier new", 16))
    but4.place(x=75, y=100)
    but5 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(5), text="5",font=("courier new", 16))
    but5.place(x=75, y=170)
    but6 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(6), text="6",font=("courier new", 16))
    but6.place(x=75, y=270)
    but7 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(7), text="7",font=("courier new", 16))
    but7.place(x=140, y=100)
    but8 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(8), text="8",font=("courier new", 16))
    but8.place(x=140, y=170)
    but9 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(9), text="9",font=("courier new", 16))
    but9.place(x=140,y=270)
    but0 = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut(0), text="0",font=("courier new", 16))
    but0.place(x=140, y=270)

    butdec = Button(screen, padx=47, pady=14, bd=4, bg="white", command=lambda: clickbut(","), text=",",font=("courier new", 16))
    butdec.place(x=75, y=310)
    butpl = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut("+"), text="+",font=("courier new", 16))
    butpl.place(x=205,y=100)
    butsub = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut("-"), text="-",font=("courier new", 16))
    butsub.place(x=205, y=170)
    butml = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut("*"), text="*",font=("courier new", 16))
    butml.place(x=205,y=240)
    butdiv = Button(screen, padx=14, pady=14, bd=4, bg="white", command=lambda: clickbut("/"), text="/",font=("courier new", 16))
    butdiv.place(x=205,y=31)
    butclear = Button(screen, padx=14, pady=119, bd=4, bg="white", command=clrbut, text="CE",font=("courier new", 16))
    butclear.place(x=270,y=100)
    butequal = Button(screen, padx=151, pady=14, bd=4, bg="white", command=equalbut,text="=",font=("courier new", 16))
    butequal.place(x=10,y=380)


screen.mainloop()
