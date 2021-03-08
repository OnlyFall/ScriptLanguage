from tkinter import *
from tkinter.filedialog import askopenfilename
filename = ''

def fileopen():
    global filename, e
    filename = askopenfilename()
    e.clear()
    e.insert(END, filename)

def handle():
    #filename = input("파일 이름 입력:")
    if filename != "":
        f = open(filename)
        content = f.read()

        histogram = [0] * 26

        new = content.lower()  # 소문자로 바꿔줌

        for c in new:
            if c.isalpha():
                histogram[ord(c) - ord('a')] += 1

        text.delete(1.0, END)
        for i in range(26):
            text.insert(END, "{0} 의 빈도수 : {1}\n".format(chr(ord('a') + i), histogram[i]))

        f.close()

    else:
        text.delete(1.0, END)
        text.insert(END, "파일을 불러오지 못했습니다.\n")


window = Tk()

frame1 = Frame(window)
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)
frame2.pack()

Label(frame2, text="파일 이름 입력").pack(side=LEFT)
e = Entry(frame2, width=20, text="")
e.pack(side=LEFT)
Button(frame2, text="열기", command=fileopen).pack(side=LEFT)
Button(frame2, text="보여주기", command=handle).pack(side=LEFT)

window.mainloop()