import pgzrun
import keyboard
#pgzrun 4k_tracker.py

FPS = 30
WIDTH = 400
HEIGHT = 500

vel = 20
back = Actor("back_1", (WIDTH // 2, HEIGHT // 2))

circle1 = Actor("circ0", center=(WIDTH/5, HEIGHT-50))
circle2 = Actor("circ0", center=(WIDTH/5*2, HEIGHT-50))
circle3 = Actor("circ0", center=(WIDTH/5*3, HEIGHT-50))
circle4 = Actor("circ0", center=(WIDTH/5*4, HEIGHT-50))

circles_1 = []
circles_2 = []
circles_3 = []
circles_4 = []

def draw():
    screen.clear()
    back.draw()

    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()

    for circle in circles_1:
        circle.draw()
    for circle in circles_2:
        circle.draw()
    for circle in circles_3:
        circle.draw()
    for circle in circles_4:
        circle.draw()

def update(dt):
    if keyboard.is_pressed("d"):
        circles_1.append(Actor("circ1", center=(WIDTH/5*1+1.40, HEIGHT-50)))
    if keyboard.is_pressed("f"):
        circles_2.append(Actor("circ1", center=(WIDTH/5*2+1.40, HEIGHT-50)))
    if keyboard.is_pressed("j"):
        circles_3.append(Actor("circ1", center=(WIDTH/5*3+1.40, HEIGHT-50)))
    if keyboard.is_pressed("k"):
        circles_4.append(Actor("circ1", center=(WIDTH/5*4+1.40, HEIGHT-50)))

    for circle in circles_1[:]:
        circle.y -= vel
        if circle.y < -50:
            circles_1.remove(circle)

    for circle in circles_2[:]:
        circle.y -= vel
        if circle.y < -50:
            circles_2.remove(circle)

    for circle in circles_3[:]:
        circle.y -= vel
        if circle.y < -50:
            circles_3.remove(circle)

    for circle in circles_4[:]:
        circle.y -= vel
        if circle.y < -50:
            circles_4.remove(circle)           

pgzrun.go()
