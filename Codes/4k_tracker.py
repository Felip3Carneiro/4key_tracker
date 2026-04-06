import pgzrun
import keyboard
import conf
#pgzrun Codes/4k_tracker.py

FPS = 30
WIDTH = 400
HEIGHT = 500

#-x-x-x-x-x-x-x-x-x-x-x-
#Configurações#
'''
1-Todos os arquivos de imagem devem estar na pasta "images"
2-Todos os nomes dos arquivos não devem ter extensões e nem números
3-Os arquivos de notas devem ser nomeados com o nome da skin + 0 ou 1 (ex: circ0, circ1)
4-Os arquivos de background devem ser nomeados com o nome do background (ex: freedom
'''

note_skin = "line" #Nome da skin das notas (ex: circ, line, round, etc...)
background = "freedom_dive"#Nome do plano de fundo (ex: freedom_dive, space, etc...)

#-x-x-x-x-x-x-x-x-x-x-x-
skin_0 = note_skin + "0"
skin_1 = note_skin + "1"

#-x-x-x-x-x-x-x-x-
print("-x-x-x-x-x-x-x-x-")
conf.skins(skin_0, skin_1, background)
print("-x-x-x-x-x-x-x-x-")
#-x-x-x-x-x-x-x-x-

back = Actor(background, (WIDTH // 2, HEIGHT // 2))

note1 = Actor(skin_0, center=(WIDTH/5, HEIGHT-50))
note2 = Actor(skin_0, center=(WIDTH/5*2, HEIGHT-50))
note3 = Actor(skin_0, center=(WIDTH/5*3, HEIGHT-50))
note4 = Actor(skin_0, center=(WIDTH/5*4, HEIGHT-50))
#WIDHT/5*x

vel = conf.vel(note1.height, note1.image)

#-x-x-x-x-x-x-x-x-x-x-x-
print("-x-x-x-x-x-x-x-x-")

print("\ngeral info:")
print(f"\nvel -> {vel}\nImages -> {skin_1}, {skin_0}\nBackground -> {background}")
print(f"\nNote height -> {note1.height}\nNote width -> {note1.width}\n")

print("-x-x-x-x-x-x-x-x-")
#-x-x-x-x-x-x-x-x-x-x-x-

notes_1 = []
notes_2 = []
notes_3 = []
notes_4 = []

def draw():
    screen.clear()
    back.draw()

    note1.draw()
    note2.draw()
    note3.draw()
    note4.draw()

    for note in notes_1:
        note.draw()
    for note in notes_2:
        note.draw()
    for note in notes_3:
        note.draw()
    for note in notes_4:
        note.draw()

def update(dt):
    if keyboard.is_pressed("d"):
        notes_1.append(Actor(skin_1, center=note1.center))
    if keyboard.is_pressed("f"):
        notes_2.append(Actor(skin_1, center=note2.center))
    if keyboard.is_pressed("j"):
        notes_3.append(Actor(skin_1, center=note3.center))
    if keyboard.is_pressed("k"):
        notes_4.append(Actor(skin_1, center=note4.center))

    for note in notes_1[:]:
        note.y -= vel
        if note.y < -50:
            notes_1.remove(note)

    for note in notes_2[:]:
        note.y -= vel
        if note.y < -50:
            notes_2.remove(note)

    for note in notes_3[:]:
        note.y -= vel
        if note.y < -50:
            notes_3.remove(note)

    for note in notes_4[:]:
        note.y -= vel
        if note.y < -50:
            notes_4.remove(note)           

pgzrun.go()
