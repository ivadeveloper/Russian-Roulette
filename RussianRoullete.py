import turtle
import random 
import math
import time

turtle.speed(0)
phi = 360/7 # Декартова система координат 
r = 50 # по этой окружности будут перемещаться патроны

def gotoxy(x, y) : 
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
def  draw_circle(r,color) :
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
def rotate(start):
    for i in range(start, random.randrange(7,25)) :
        phi_rad = phi * i * math.pi / 180 # формулы sin и cos в Пайтоне работают с радианами 
        gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
        draw_circle(21, 'brown')
        draw_circle(21, 'white')

    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    draw_circle(21, 'brown')
    return i % 7 

gotoxy(0,0) 
turtle.circle(80)
gotoxy(0,160)
draw_circle(5, 'red') 

gotoxy(285,-356)
turtle.write('Russian Roulette', font=('Avenir', 30, 'bold'))
gotoxy(285,-400)
turtle.write('10A Labs', font=('Avenir', 30, 'bold'))
gotoxy(285,-444)
turtle.write('Ver 2.0', font=('Avenir', 30, 'bold'))

    
for i in range(0,7) :
    phi_rad = phi * i * math.pi / 180 # формулы sin и cos в Пайтоне работают с радианами 
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    draw_circle(21, 'white')


players_number = int(input('Number of players: '))
alive  = [str(input()) for z in range(players_number)]

print(alive)

killed = 'str'

dead = []

answer = ' '

w = 0

start = 0
while answer != 'no' :
    answer = turtle.textinput(f'Играет {alive[w]}?', 'yes/no')

    t2 = turtle.Turtle()
    t2.setpos(-585,-400)
    t2.write(f'Alive: {alive}', font=('Avenir', 28, 'bold'))
    t3 = turtle.Turtle()
    t3.setpos(-585,-444)
    t3.write(f'Dead: {dead}', font=('Avenir', 28, 'bold'))
    
    if answer == 'yes':
        start = rotate(start)
        if w == players_number-1:
            w = 0
        else:
            w +=1
        if start  == 0 :
            t1 = turtle.Turtle()
            t1.setpos(-170,250)
            t1.write(f'Удача отвернулась от {alive[w]}!', font=('Avenir', 28, 'bold'))
            time.sleep(1)
            dead.append(alive[w])
            killed = alive[w]
            alive.remove(killed)
            players_number -=1
            t1.clear()
            if players_number == 1:  
                t4 = turtle.Turtle()
                t4.setpos(-170,250)
                t4.write('CONGRATULATIONS', font=('Avenir', 28, 'bold'))
                break
            
        if w > players_number-1:
            w = 0
    else:
        if w > players_number-1:
            w = 0
        pass
    t2.clear()
    t3.clear()


