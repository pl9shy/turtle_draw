import turtle

t = turtle.Turtle(visible=False)
s = turtle.Screen()
s.setup(1.0, 1.0)

colors_in_russian = {  # Словарь цветов для использования на русском языке.
    'красный': 'red',
    'тёмно-красный': 'dark red',
    'коралловый': 'Coral',
    'томатный': 'tomato',
    'малиновый': 'Crimson',
    'розовато-коричневый': 'rosy brown',
    'глубокий розовый': 'deep pink',
    'фиолетовый': 'Purple',
    'сиреневый': 'violet',
    'сливовый': 'Plum',
    'индиго': 'Indigo',
    'лавандовый': 'Lavender',
    'оранжевый': 'orange',
    'светло-жёлтый': 'light yellow',
    'золотой': 'gold',
    'бежевый': 'tan',
    'коричневый': 'SaddleBrown',
    'кирпичный': 'Firebrick',
    'жёлтый': 'yellow',
    'зелёный': 'green',
    'тёмно-зелёный': 'sea green',
    'светло-зелёный': 'light green',
    'лаймовый': 'Lime',
    'жёлто-зелёный': 'yellow green',
    'оливковый': 'OliveDrab',
    'синий': 'MediumBlue',
    'тёмно-синий': 'DarkSlateBlue',
    'голубой': 'sky blue',
    'белый': 'white',
    'серый': 'gray',
    'чёрный': 'black',
    'розовый': 'pink',
    'аквамариновый': 'aquamarine',
}

colors_list = list(colors_in_russian)
real_shape = 'square'
real_color = 'black'
real_size = 50
real_background = 'white'


def get_coordinates(x, y):
    '''
Воспроизводит несколько функций.
    '''
    get_figures(x, y)
    list_of_colors(x, y)
    get_options(x, y)


def get_figures(x, y):
    '''
Определить текущую фигуру.
    '''
    global real_shape
    if -250 <= x <= -230 and 330 <= y <= 350:
        real_shape = 'square'
    if -210 <= x <= -190 and 330 <= y <= 350:
        real_shape = 'triangle'
    if -170 <= x <= -150 and 330 <= y <= 350:
        real_shape = 'circle'
    if -130 <= x <= -110 and 330 <= y <= 350:
        real_shape = 'line'
    if -90 <= x <= -70 and 330 <= y <= 350:
        real_shape = 'star'


def list_of_colors(x, y):
    '''
Печатает доступные цвета при нажатии на кнопку "Цвет".
    '''
    if -360 <= x <= -320 and 330 <= y <= 350:
        print(f'Список доступных цветов: {sorted(colors_list)}')


def get_options(x, y):
    '''
Учитывает параметры для отрисовки фигуры. (цвет, размер, ластик, фон, очистка холста)
    '''
    if -360 <= x <= -320 and 330 <= y <= 350:  # Изменяет цвет фигуры.
        global real_color
        r_color = str(s.textinput('Цвет пера', 'Задайте цвет пера: '))
        for k, v in colors_in_russian.items():  # Перебирает значения словаря, меняет цвет кнопки.
            if k == r_color:
                real_color = v
                t.pensize(1)
                t.penup()
                t.goto(-360, 330)
                t.setheading(0)
                t.pendown()
                if real_color == 'black':
                    t.pencolor('white')
                else:
                    t.pencolor('black')
                t.fillcolor(real_color)
                t.begin_fill()
                for i in range(2):
                    t.fd(40)
                    t.left(90)
                    t.fd(20)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.goto(-355, 332)
                t.write('Цвет', font=('Verdana', 10, 'normal'))
    if -310 <= x <= -270 and 330 <= y <= 350:  # Меняет текущую фигуру на ластик.
        global real_shape
        real_shape = 'eraser'
    if -410 <= x <= -370 and 330 <= y <= 350:  # Изменяет размер фигуры.
        global real_size
        real_size = int(s.textinput('Размер пера', 'Задайте размер пера: '))
    if -460 <= x <= -420 and 330 <= y <= 350:  # Изменяет цвет холста.
        global real_background
        r_background = str(s.textinput('Цвет холста', 'Задайте цвет холста: '))
        for k, v in colors_in_russian.items():
            if k == r_background:
                real_background = v
                s.bgcolor(real_background)
                t.clear()
                buttons()
    if -510 <= x <= -470 and 330 <= y <= 350:  # Очистка холста.
        t.clear()
        buttons()


def blanks(x, y):
    '''
Заготовки для отрисовки фигуры.
    '''
    centered_figures(x, y)
    t.color(real_color)
    t.width(int(real_size / 25))
    t.setheading(0)
    t.up()
    t.goto(xc, yc)
    t.down()
    t.setheading(0)
    t.fillcolor(real_color)


def centered_figures(x, y):
    '''
Клик мыши принимается за центр фигуры, т.е рисуется не от угла, а от оси.
    '''
    global xc, yc
    num_del = 2  # Число-делитель, для ровного и пропорционального построения фигуры.
    if real_shape == 'square':
        xc = x + real_size / num_del
        yc = y + real_size / num_del
    if real_shape == 'triangle':
        xc = x - real_size / num_del
        yc = y - real_size / num_del
    if real_shape == 'circle':
        xc = x
        yc = y - real_size / num_del
    if real_shape == 'star':
        xc = x - real_size / num_del
        yc = y + real_size / (num_del * 3)


def square(x, y):
    '''
Отрисовка квадрата.
    '''
    blanks(x, y)
    t.left(90)
    t.begin_fill()
    for _ in range(4):
        t.left(90)
        t.fd(real_size)
    t.end_fill()


def triangle(x, y):
    '''
Отрисовка треугольника.
    '''
    blanks(x, y)
    t.begin_fill()
    for _ in range(3):
        t.fd(real_size)
        t.left(120)
    t.end_fill()


def circle(x, y):
    '''
Отрисовка круга.
    '''
    blanks(x, y)
    t.begin_fill()
    t.circle(real_size / num_del)
    t.end_fill()


def sixangle(x, y):
    '''

    '''


def star(x, y):
    '''
Отрисовка звезды.
    '''
    blanks(x, y)
    t.begin_fill()
    for _ in range(5):
        t.forward(real_size)
        t.rt(144)
    t.end_fill()


def eraser(x, y):
    '''
Отрисовка ластика (точка, цвет которой совпадает с цветом текущего фона.).
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(real_size * num_del, real_background)


def click_draw(x, y):
    '''
Вызывает функции, которые в дальнейшем отрисовывают текущую фигуру.
    '''
    if real_shape == 'square':
        square(x, y)
    if real_shape == 'triangle':
        triangle(x, y)
    if real_shape == 'circle':
        circle(x, y)
    if real_shape == 'star':
        star(x, y)
    if real_shape == 'eraser':
        eraser(x, y)


def buttons():
    '''
Отрисовка кнопок, с помощью которых пользователь взаимодействует с программой.
    '''
    turtle.tracer(0)
    t.pensize(1)
    t.setheading(0)
    t.color('black')
    t.penup()  # Кнопка "Ластик".
    t.goto(-310, 330)
    t.pendown()
    if real_background == 'black':  # Если фон чёрный, контур кнопок - белый.
        t.pencolor('white')
    else:  # В других случаях контур кнопок - чёрный.
        t.pencolor('black')
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(2):
        t.fd(40)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-307, 334)
    t.write('Ластик', font=('Verdana', 7, 'normal'))

    t.penup()  # Кнопка "Цвет".
    t.goto(-360, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(2):
        t.fd(40)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-355, 332)
    t.write('Цвет', font=('Verdana', 10, 'normal'))

    t.penup()  # Кнопка "Размер".
    t.goto(-410, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(2):
        t.fd(40)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-408, 334)
    t.write('Размер', font=('Verdana', 7, 'normal'))

    t.penup()  # Кнопка "Фон".
    t.goto(-460, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(2):
        t.fd(40)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-453, 332)
    t.write('Фон', font=('Verdana', 10, 'normal'))

    t.penup()  # Кнопка "Очистить".
    t.goto(-510, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(2):
        t.fd(40)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-507, 334)
    t.write('Очистить', font=('Verdana', 6, 'normal'))

    t.penup()  # Кнопка "Квадрат".
    t.goto(-250, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(4):
        t.fd(20)
        t.left(90)
    t.end_fill()

    t.penup()  # Кнопка "Треугольник".
    t.goto(-210, 330)
    t.pendown()
    if real_background == 'black':
        t.pencolor('white')
    else:
        t.pencolor('black')
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(3):
        t.fd(20)
        t.left(120)
    t.end_fill()

    t.penup()  # Кнопка "Треугольник".
    t.goto(-160, 330)
    t.pendown()
    t.fillcolor(real_background)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()  # Кнопка "Шестиугольник".
    t.goto(-127, 350)
    t.down()
    for _ in range(6):
        t.fd(12)
        t.rt(60)

    t.penup()  # Кнопка "Звезда".
    t.goto(-73, 330)
    t.pendown()
    t.setheading(144)
    t.fillcolor(real_background)
    t.begin_fill()
    for i in range(5):
        t.forward(23)
        t.rt(144)
    t.end_fill()
    turtle.tracer(1)
    t.speed(0)


buttons()

turtle.listen()

turtle.onscreenclick(get_coordinates, 1)
turtle.onscreenclick(click_draw, 3)

s.mainloop()
