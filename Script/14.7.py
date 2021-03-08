from tkinter import *
from tkinter.filedialog import askopenfilename
filename = ''

def fileopen():
    global filename, e
    filename = askopenfilename()
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

    maxCount = max(histogram)
    barW = (500 - 10 - 10) / 26 # 막대 그래프 하나의 width

    canvas.delete('grim')
    for i in range(26):
        canvas.create_rectangle(10 + i * barW, 20 + 180 * (1 - histogram[i] / maxCount), 10 + (i + 1) * barW, 190, tags='grim')
        canvas.create_text(10 + i * barW + 10, 190 + 5, text=chr(i + ord('a')), tags='grim')
        canvas.create_text(i * barW + 20, 20 + 180 * (1 - histogram[i] / maxCount) - 7 , text=histogram[i], tags="grim")



window = Tk()

frame1 = Frame(window)
frame1.pack()

canvas = Canvas(frame1, width=500, height=200, bg='white')
canvas.pack()

frame2 = Frame(window)
frame2.pack()

Label(frame2, text="파일 이름 입력").pack(side=LEFT)
e = Entry(frame2, width=20, text="")
e.pack(side=LEFT)

Button(frame2, text="열기", command=fileopen).pack(side=LEFT)
Button(frame2, text="보여주기", command=handle).pack(side=LEFT)

window.mainloop()