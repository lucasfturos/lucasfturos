from tkinter import mainloop
import turtle

turtle.speed(0)


def fleur():
    for i in range(360):
        turtle.circle(190 - i, 90)
        turtle.left(90)
        turtle.circle(190 - i, 90)
        turtle.left(18)


fleur()
mainloop()
