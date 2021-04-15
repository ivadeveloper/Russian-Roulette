import turtle
import random 
import math
import time

turtle.speed(0)
phi = 360/7  # Декартова система координат
r = 50  # по этой окружности будут перемещаться патроны


screen = turtle.Screen()
image = "background.gif"
screen.setup(1920, 1080)
screen.addshape(image)
screen.bgpic(image)


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def  draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def rotate(start):
    for i in range(start, random.randrange(7, 25)):
        phi_rad = phi * i * math.pi / 180  # формулы sin и cos в python работают с радианами
        gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
        draw_circle(21, 'brown')
        draw_circle(21, '#746f6a')


    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    draw_circle(21, 'brown')
    return i % 7 

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
draw_circle(5, 'red')


t5 = turtle.Turtle()
t5.setpos(437, 437)
t5.color("#642214")
t5.write('Ver 2.1', font=('Myriad Pro', 30, 'bold'))

    
for i in range(0,7) :
    phi_rad = phi * i * math.pi / 180  # формулы sin и cos в python работают с радианами
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    draw_circle(21, 'white')


players_number = int(turtle.numinput('Количество игрков:', '', 5))
alive = turtle.textinput('Имена игроков: ', 'через пробел').split()

print(alive)

killed = 'str'

dead = []

answer = ' '

w = 0

t2 = turtle.Turtle()
t3 = turtle.Turtle()

start = 0
while answer != 'no' :
    answer = turtle.textinput(f'Играет {alive[w]}?', 'yes/no')

    t2 = turtle.Turtle()
    t2.setpos(-585, -444)
    t2.color("#f28f18")
    t2.write(f'Alive: {alive}', font=('Myriad Pro', 28, 'bold'))
    t3.setpos(-585, -488)
    t3.color("#f28f18")
    t3.write(f'Dead: {dead}', font=('Myriad Pro', 28, 'bold'))
    
    if answer == 'yes':
        start = rotate(start)
        if w == players_number-1:
            w = 0
        else:
            w +=1
        if start == 0 :
            t1 = turtle.Turtle()
            t1.setpos(-170, 250)
            t1.write(f'Удача отвернулась от {alive[w]}!', font=('Myriad Pro', 28, 'bold'))
            time.sleep(1)
            dead.append(alive[w])
            killed = alive[w]
            alive.remove(killed)
            players_number -=1
            t1.clear()
            if players_number == 1:  
                t4 = turtle.Turtle()
                t4.setpos(-170, 250)
                t4.write('CONGRATULATIONS', font=('Myriad Pro', 28, 'bold'))
                time.sleep(5)
                break
            
        if w > players_number-1:
            w = 0
    else:
        if w > players_number-1:
            w = 0
        pass
    t2.clear()
    t3.clear()
