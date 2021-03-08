from tkinter import *

#def process():
#    dollar = eval(e1.get())
#    e2.insert(0, str(dollar*1200))


#window = Tk()
#window.title("파이썬 윈도우")
#l1 = Label(window, text="달러", font="helvetica 16 italic")
#l2 = Label(window, text="원", font="helvetica 16 italic")

#l1.grid(row=0, column = 0, sticky = "W")
#l2.grid(row=1, column = 0, sticky = "W")

#e1 = Entry(window, bg='yellow', fg='black')
#e2 = Entry(window, bg='blue', fg='white')

#e1.grid(row=0, column = 1)
#e2.grid(row=1, column = 1)

#b1 = Button(window, text="달러 -> 원", command=process, font="helvetica 16 italic")
#b2 = Button(window, text="원 -> 달러", command=process)

#b1.grid(row=2, column = 0); b1.configure(font='helveticca 12')
#b2.grid(row=2, column = 1); b2["bg"] = "green"

#window.mainloop()


from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image = img


window = Tk()

photo = PhotoImage(file="우주소녀.gif")

imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='클릭', command=change_img)
button.pack()

window.mainloop()
