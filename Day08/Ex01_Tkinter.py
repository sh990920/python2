'''
tkinter
    파이썬에서 기본적으로 제공하는 GUI(Graphical User Interface) 프로그램 모듈
    tkinter 모듈은 간단하게 GUI 프로그램을 만들기 좋다
    다른 GUI 모듈 : pyQt
'''
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# 주석부분은 html 태그
# label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# input text
entry = tk.Entry(root)
entry.pack()

# textarea 
text = tk.Text(root)
text.pack()

# input checkBox
checkbox_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me!", variable=checkbox_var)
checkbutton.pack()

# input radio
var = tk.StringVar()
var.set("option1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="option1")
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="option2")
radiobutton1.pack()
radiobutton2.pack()

# input range
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.pack()

# input number
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# select
combo = ttk.Combobox(root, values=["Item1", "Item2", "Item3"])
combo.pack()

def onClick():
    s_entry = entry.get()
    s_text = text.get("1.0", tk.END)
    s_rediobutton = var.get()
    s_checkbox_var = checkbox_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()

    print("button Click!")
    print(f"s_entry : {s_entry}")
    print(f"s_text : {s_text}")
    print(f"s_rediobutton : {s_rediobutton}")
    print(f"s_checkbox_var : {s_checkbox_var}")
    print(f"i_scale : {i_scale}")
    print(f"i_spinbox : {i_spinbox}")
    print(f"s_combo : {s_combo}")

# input button
button = tk.Button(root, text="Click me!", command=onClick)
button.pack()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

line = canvas.create_line(0, 0, 200, 200)
rect = canvas.create_rectangle(50, 50, 150, 150, fill="red")

# 실행 코드
root.mainloop()