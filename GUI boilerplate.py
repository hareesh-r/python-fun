from tkinter import *
import tkinter.font as font

def GUI_getinput(test_string):
    arr = []
    def func():
        string  = str(reg.get())
        arr.append(string)
        screen.destroy()

    global screen
    screen = Tk()

    screen.title("Type and click Enter button")

    screen.geometry("665x470")

    screen.config(bg="dim grey")

    myFont = font.Font(weight="bold")

    Label(text = test_string  , fg="white" ,font = myFont, bg = "dodger blue" , width = "150" , height = "3" ).pack()

    reg = Entry(screen,text = "Regulation Year",width="50",justify=CENTER)

    reg.focus_set()
    
    reg.pack(pady = "10" , padx = "10",ipady=5)

    btn = Button(text = "Enter",width="15",fg="grey17",bg = "white", command = func)

    btn.pack(ipady=5)

    screen.mainloop()
    return arr[-1]

print(GUI_getinput("Enter regulation 2017 or 2013 for"))