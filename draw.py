import tkinter as tk
import turtle as t
from tkinter import colorchooser
from tkinter import ttk



current_size = 50
current_color = "black"
current_shape = "Квадрат"

def draw_shape(x, y):
    turtle_pen.penup()
    turtle_pen.pencolor(current_color)
    turtle_pen.fillcolor(current_color)

    if current_shape == "Квадрат":
        centered_square(x,y)
        turtle_pen.goto(current_x, current_y)
        turtle_pen.pendown()
        turtle_pen.begin_fill()
        
        for _ in range(4):
            turtle_pen.right(90)
            turtle_pen.forward(current_size) 
        turtle_pen.end_fill()
            
    elif current_shape == "Треугольник":
        centered_triangle(x, y)
        turtle_pen.goto(current_x, current_y)
        turtle_pen.pendown()
        turtle_pen.begin_fill()
        for _ in range(3):
            turtle_pen.forward(current_size) 
            turtle_pen.left(120)
        turtle_pen.end_fill()

    elif current_shape == "Круг":
        centered_circle(x, y)
        turtle_pen.goto(current_x, current_y)
        turtle_pen.pendown()
        turtle_pen.begin_fill()
        turtle_pen.circle(current_size / 2)  
        turtle_pen.end_fill()

    elif current_shape == "Шестиугольник":
        centered_hexagon(x, y)
        turtle_pen.goto(current_x, current_y)
        turtle_pen.pendown()
        turtle_pen.begin_fill()
        for _ in range(6):
            turtle_pen.forward(current_size / 1.6) 
            turtle_pen.right(60)
        turtle_pen.end_fill()

    elif current_shape == "Звезда":
        centered_star(x, y)
        turtle_pen.goto(current_x, current_y)
        turtle_pen.pendown()
        turtle_pen.begin_fill()
        for _ in range(5):
            turtle_pen.forward(current_size)  
            turtle_pen.right(144)
        turtle_pen.end_fill()

def centered_square(x, y):
    global current_x, current_y
    current_x = x + current_size / 1.5
    current_y = y + current_size / 2 

def centered_triangle(x, y):
    global current_x, current_y
    current_x = x - current_size / 3
    current_y = y - current_size / 2

def centered_circle(x, y):
    global current_x, current_y
    current_x = x + current_size / 4.5
    current_y = y - current_size / 2

def centered_hexagon(x, y):
    global current_x, current_y
    current_x = x - current_size / 4.5
    current_y = y + current_size / 2

def centered_star(x, y):
    global current_x, current_y
    current_x = x - current_size / 3
    current_y = y + current_size / 12

def size_message():
    global current_size                                                                            # Отображение текущей фигуры
    message = tk.Label(win, text= f"Текущий размер: {round(current_size)}", bg="white", fg="black", width=25, height=1)
    #message.pack(side=tk.RIGHT)
    message.pack(side=tk.TOP)
    message.after(1700, message.destroy)

def change_color():
    global current_color                                                                                       # Изменяет цвет кисти
    color_code = colorchooser.askcolor(title="Выберите цвет")
    if color_code[1] == '#000000':
        t.color = color_code[1]
        color_button.config(bg=color_code[1], fg="white")
        current_color = color_code[1]
    else:
        t.color = color_code[1]
        color_button.config(bg=color_code[1], fg="black")
        current_color = color_code[1]

def change_background():                                                                                              # Изменяет цвет фона
    color_code = colorchooser.askcolor(title="Выберите цвет фона")
    if color_code[1] == '#000000':
        win.configure(bg=color_code[1])
        t_screen.bgcolor(color_code[1])
        for button in buttons:
            button.config(bg=color_code[1], fg="white")
    else:
        win.configure(bg=color_code[1])
        t_screen.bgcolor(color_code[1])
        for button in buttons:
            button.config(bg=color_code[1], fg="black")

def callback(*arg):
    global current_shape           
    current_shape = shape_combobox.get()

def clear_canvas():
    turtle_pen.clear()

def change_size():
    global current_size
    current_size = t_screen.numinput("Введите размер", "Текущий размер:", minval=10, maxval=1000)
    size_message()

win = tk.Tk()
win.title('Turtle Draw')
win.configure(bg = 'white')
win.geometry("1200x800+350+100")

canvas = t.ScrolledCanvas(win)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

t_screen = t.TurtleScreen(canvas)

turtle_pen = t.RawTurtle(t_screen)
turtle_pen.speed(0)

t_screen.onclick(draw_shape, 1)

clear_button = tk.Button(text="Очистить", bg = "white", fg= "black", borderwidth=2, width=10, height=1, command=clear_canvas) #Кнопка "Очистить"
clear_button.pack(anchor = "s")
 
background_button = tk.Button(text="Фон", bg = "white", fg= "black", borderwidth=2 ,command=change_background, width=10, height=1) #Кнопка "Фон"
background_button.pack(anchor = "s")
 
size_button =tk.Button(text="Размер", bg = "white", fg= "black", borderwidth=2 ,width=10, height=1, command= change_size) #Кнопка "Размер" 
size_button.pack(anchor = "s")

color_button = tk.Button(text="Цвет", bg = "white", fg= "black", borderwidth=2, command=change_color, width=10, height=1) #Кнопка "Цвет"
color_button.pack(anchor = "s")

var = tk.StringVar()

shapes = ["Квадрат", "Треугольник", "Круг", "Шестиугольник", "Звезда"]
shape_combobox = ttk.Combobox(win, values=shapes, textvariable = var)
shape_combobox.set("Квадрат")
shape_combobox.pack(side=tk.TOP)

var.trace('w', callback)

buttons = [background_button, clear_button, size_button]

win.mainloop()
