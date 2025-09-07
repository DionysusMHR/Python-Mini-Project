from tkinter import *



def add_display_0():
    display_text.set(display_text.get()+'0')

def add_display_1():
    display_text.set(display_text.get()+'1')

def add_display_2():
    display_text.set(display_text.get()+'2')

def add_display_3():
    display_text.set(display_text.get()+'3')

def add_display_4():
    display_text.set(display_text.get()+'4')

def add_display_5():
    display_text.set(display_text.get()+'5')

def add_display_6():
    display_text.set(display_text.get()+'6')

def add_display_7():
    display_text.set(display_text.get()+'7')

def add_display_8():
    display_text.set(display_text.get()+'8')

def add_display_9():
    display_text.set(display_text.get()+'9')

def add_display_dot():
    display_text.set(display_text.get()+'.')

def add_display_plus():
    display_text.set(display_text.get()+'+')

def add_display_minus():
    display_text.set(display_text.get()+'-')

def add_display_multiply():
    display_text.set(display_text.get()+'*')

def add_display_divid():
    display_text.set(display_text.get()+'/')

def add_display_mod():
    display_text.set(display_text.get()+'%')

def add_display_power():
    display_text.set(display_text.get()+'**')

def add_display_clear():
    display_text.set('')

def add_display_equal():
    display_text.set(eval(display_text.get()))



if __name__ == "__main__":
    
    root = Tk()
    root.title("mhr_calculator")
    root.resizable(width=False, height=False)
    

    display_frame = Frame(root)
    display_frame.pack()

    display_text = StringVar()
    display_lbl = Label(display_frame, textvariable=display_text, height=4, width=25, relief='sunken',
                        borderwidth=10, bg='#D8D2C2', font=('Time', 20))
    display_lbl.pack()


    btn_frame = Frame(root)
    btn_frame.pack()

    btn_clear = Button(btn_frame, text='Clear', font=('Time', 20), height=2, width=5, command=add_display_clear)
    btn_clear.grid(row=0, column=0, sticky=NW)

    btn_mod = Button(btn_frame, text='%', font=('Time', 20), height=2, width=5, command=add_display_mod)
    btn_mod.grid(row=0, column=1, sticky=NW)

    btn_power = Button(btn_frame, text='**', font=('Time', 20), height=2, width=5, command=add_display_power)
    btn_power.grid(row=0, column=2, sticky=NW)

    btn7 = Button(btn_frame, text='7', font=('Time', 20), height=2, width=5, command=add_display_7)
    btn7.grid(row=1, column=0, sticky=NW)

    btn8 = Button(btn_frame, text='8', font=('Time', 20), height=2, width=5, command=add_display_8)
    btn8.grid(row=1, column=1, sticky=NW)

    btn9 = Button(btn_frame, text='9', font=('Time', 20), height=2, width=5, command=add_display_9)
    btn9.grid(row=1, column=2, sticky=NW)

    btn_minus = Button(btn_frame, text='-', font=('Time', 20), height=2, width=5, command=add_display_minus)
    btn_minus.grid(row=1, column=3, sticky=NW)

    btn4 = Button(btn_frame, text='4', font=('Time', 20), height=2, width=5, command=add_display_4)
    btn4.grid(row=2, column=0, sticky=NW)

    btn5 = Button(btn_frame, text='5', font=('Time', 20), height=2, width=5, command=add_display_5)
    btn5.grid(row=2, column=1, sticky=NW)

    btn6 = Button(btn_frame, text='6', font=('Time', 20), height=2, width=5, command=add_display_6)
    btn6.grid(row=2, column=2, sticky=NW)

    btn_plus = Button(btn_frame, text='+', font=('Time', 20), height=2, width=5, command=add_display_plus)
    btn_plus.grid(row=2, column=3, sticky=NW)

    btn1 = Button(btn_frame, text='1', font=('Time', 20), height=2, width=5, command=add_display_1)
    btn1.grid(row=3, column=0, sticky=NW)

    btn2 = Button(btn_frame, text='2', font=('Time', 20), height=2, width=5, command=add_display_2)
    btn2.grid(row=3, column=1, sticky=NW)

    btn3 = Button(btn_frame, text='3', font=('Time', 20), height=2, width=5, command=add_display_3)
    btn3.grid(row=3, column=2, sticky=NW)

    btn_multiply = Button(btn_frame, text='*', font=('Time', 20), height=2, width=5, command=add_display_multiply)
    btn_multiply.grid(row=3, column=3, sticky=NW)

    btn_zero = Button(btn_frame, text='0', font=('Time', 20), height=2, width=5, command=add_display_0)
    btn_zero.grid(row=4, column=0, sticky=NW)

    btn_dot = Button(btn_frame, text='.', font=('Time', 20), height=2, width=5, command=add_display_dot)
    btn_dot.grid(row=4, column=1, sticky=NW)

    btn_equal = Button(btn_frame, text='=', font=('Time', 20), height=2, width=5, command=add_display_equal)
    btn_equal.grid(row=4, column=2, sticky=NW)

    btn_divid = Button(btn_frame, text='/', font=('Time', 20), height=2, width=5, command=add_display_divid)
    btn_divid.grid(row=4, column=3, sticky=NW)


    root.mainloop()


# bug zero left