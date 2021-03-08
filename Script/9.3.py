from tkinter import *

class Radio:
    def __init__(self):
        window =Tk()
        window.title("라디오 버튼")
        self.canvas = Canvas(window, bg="white", width=300, height=200)
        self.canvas.create_rectangle(10, 10, 290, 190, tags="Grim")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.v = IntVar()  #self.v.get()해서 값 알아낼 예정
        Radiobutton(frame, text="직사각형", variable=self.v, value=1,command=self.display).pack(side=LEFT)
        Radiobutton(frame, text="타원", variable=self.v, value=2, command=self.display).pack(side=LEFT)

        self.f = IntVar()
        Checkbutton(frame, text="채우기", variable=self.f, command=self.display).pack(side=LEFT)
        window.mainloop()

    def display(self):
        self.canvas.delete("Grim")

        if self.v.get() == 1: # 직사각형
            if self.f.get() == 1:
                self.canvas.create_rectangle(10, 10, 290, 190, tags="Grim", fill='blue')
            else:
                self.canvas.create_rectangle(10, 10, 290, 190, tags="Grim")
        else: # 타원
            if self.f.get() == 1:
                self.canvas.create_oval(10, 10, 290, 190, tags="Grim", fill='blue')
            else:
                self.canvas.create_oval(10, 10, 290, 190, tags="Grim")

Radio()


