from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# 다각형
canvas.create_polygon(250, 400, 275, 450, 225, 450)

# 캔버스에서 화면이 움직이게 하기위해서 for 문 작성
for i in range(0, 70):

    canvas.move(1, 0, -5)
    
    tk.update()
    
    time.sleep(0.05)