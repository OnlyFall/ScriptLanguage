from tkinter import *


class Ball:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.dx = 2
        self.dy = 2


class BallAnimator:
    def __init__(self):
        window = Tk()
        window.title("공튀기기")

        self.width = 500
        self.height = 300
        self.canvas = Canvas(window, bg='white', width=self.width, heigh=self.height)
        self.canvas.pack()
        self.ballList = []
        self.speed = 100
        self.on = True
        frame = Frame(window)
        frame.pack()

        Button(frame, text="정지", command=self.stop).pack(side=LEFT)
        Button(frame, text="재시작", command=self.resume).pack(side=LEFT)
        Button(frame, text="+", command=self.add).pack(side=LEFT)
        Button(frame, text="-", command=self.sub).pack(side=LEFT)
        Button(frame, text="빠르게", command=self.faster).pack(side=LEFT)
        Button(frame, text="느리게", command=self.slower).pack(side=LEFT)

        self.animate()
        window.mainloop()

    def animate(self):
        while self.on:
            self.canvas.after(self.speed)
            self.canvas.update()
            self.canvas.delete("ball")
            for ball in self.ballList:
                if ball.x >= self.width or ball.x < 0:
                    ball.dx *= -1
                if ball.y >= self.height or ball.y <= 0:
                    ball.dy *= -1
                ball.x += ball.dx
                ball.y += ball.dy
                self.canvas.create_oval(ball.x - 3, ball.y - 3, ball.x + 3, ball.y + 3, fill='red', tags="ball")

    def stop(self):
        self.on = False

    def resume(self):
        self.on = True
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def sub(self):
        self.ballList.pop()

    def faster(self):
        self.speed -= 5

    def slower(self):
        self.speed += 5

BallAnimator()
