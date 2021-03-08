from tkinter import *


def result():
    money = float(e1.get())
    year = float(e2.get())
    interest = float(e3.get())
    futureValue = money * ((1 + interest/100)**(year + 12))
    #l5.configure(text=str(futureValue))
    l5.configure(text="{0:.2f}".format(futureValue))


window = Tk()

l1 = Label(window, text="투자금").grid(row=0, column=0, sticky="W")
l2 = Label(window, text="기간(년)").grid(row=1, column=0, sticky="W")
l3 = Label(window, text="월이율(%)").grid(row=2, column=0, sticky="W")
l4 = Label(window, text="미래가치").grid(row=3, column=0, sticky="W")

l5 = Label(window, text="")
l5.grid(row=3, column=1, sticky="E")

e1 = Entry(window, justify=RIGHT)
e1.grid(row=0, column=1)

e2 = Entry(window, justify=RIGHT)
e2.grid(row=1, column=1)

e3 = Entry(window, justify=RIGHT)
e3.grid(row=2, column=1)

Button(window, text="계산하기", command=result).grid(row=4, column=1, sticky='E')
window.mainloop()