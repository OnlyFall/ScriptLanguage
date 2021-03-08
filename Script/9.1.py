from tkinter import *

leftPosition = 10
topPosition = 10
rightPosition = 20
bottomPosition = 20

def common(index):
    global leftPosition, topPosition, rightPosition, bottomPosition

    if index == 0: #상
        if topPosition <= 10:
            pass
        else:
            bottomPosition -= 5
            topPosition -= 5

    elif index == 1: #하
        if bottomPosition >= 190:
            pass
        else:
            bottomPosition += 5
            topPosition += 5

    elif index == 2: #좌
        if rightPosition <= 20:
            pass
        else:
            rightPosition -= 5
            leftPosition -= 5

    elif index == 3: #우
        if rightPosition >= 280:
            pass
        else:
            rightPosition += 5
            leftPosition += 5

    canvas.delete("ball")
    canvas.create_oval(leftPosition, topPosition, rightPosition, bottomPosition, fill='red', tags='ball')


window = Tk()

canvas = Canvas(window, width=300, height=200, bg='white')
canvas.pack()
canvas.create_oval(10, 10, 20, 20, fill='red', tags='ball')

frame = Frame(window)
frame.pack()   #프레임을 윈도우 안에 배치함

outText = ['UP', 'DOWN', 'LEFT', 'RIGHT']
for i in range(4):
    Button(frame, text=str(outText[i]), command=lambda index=i: common(index)).pack(side=LEFT)
    print(i)

window.mainloop()