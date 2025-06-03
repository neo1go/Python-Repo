from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 50 # Pixelgröße für alle Spielelemente, also dem Essen sowie dem Schlangenelement. Die wichtigste Einheit, die die ganze Zeit addiert oder subtrahiert wird.
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"  # blau ist "#0000FF"
FOOD_COLOR = "#FF0000"   # gelb ist "#FFFF00"
BACKGROUND_COLOR = "#000000"   # weiß ist "#FFFFFF"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []  # Enthält nur die Koordinaten im Grid. Diese dienen der Schlangenposition. Wenn ein Element hinzukommt, wird auch diese List 
                               # erweitert wegen der Bewegung der gesamten Schlange. Außerdem kann man so die Kollisionen prüfen, mit sich selbst und dem Rand natürlich.
                               
        self.squares = []      # Der Körper der Schlange. Enthält eine Liste con Canvas-Objekten wie z.B. die Rechtecke des Körpers
        
        for i in range(0, BODY_PARTS): #3
            self.coordinates.append([0, 0])  # Startpunkt ist 0,0
            
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")# das Bodypart-Objekt der Schlange
            self.squares.append(square)   # hier wird das erste Bodypart-Objekt gesetzt an der entsprechenden Koordinate.

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1)* SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1)* SPACE_SIZE
        
        self.coordinates = [x, y]
        
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food") # Anfangs- und Endpunkte für das Objekt Food
        
        
# dies passiert bei jedem neuen Frame
def next_turn(snake, food):  
    x, y = snake.coordinates[0]  #coordinates[0] ist die Position des Kopfes der Schlange werden hier entpackt.
    
    if direction == "up":   # jeweils 50 px in die entsprechende Richtung
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x, y))  # neue Position des Kopfes der Schlange nach der Bewegung
    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)  # ein neues Element wird gezeichnet an neuer Stelle mit Anfang und Endkoordinaten
    
    snake.squares.insert(0, square)  # dies ist der neue Eintrag in die List als neuer Kopf mit den neuen Koordinaten sozusagen. Da ja die Position um eins verändert wurde.
    
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()   # erzeugt neues random Food-Objekt
    else:
        del snake.coordinates[-1] # durch die Weiterbewegung muß die letzte Koordinate der Schlange gelöscht werden aus der List, also das Schwanzende.
        
        canvas.delete(snake.squares[-1])# es muß auch das visuelle Gebilde des Schwanzes entfernt werden im canvas. 
        
        del snake.squares[-1]  # hier wird das letzte Element aus der List gelöscht
    
    if check_collisions(snake):
        game_over()
    else:  
        window.after(SPEED, next_turn, snake, food) # hier wird die Funktion nach der Verzögerung SPEED erneut aufgerufen.
    
    

def change_direction(new_direction):
    global direction    # alte Richtung

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up': 
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down': 
        if direction != 'up':
            direction = new_direction
        
        
def check_collisions(snake):
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("Snake game")
window.resizable(False, False)   # für x und y Richtung seperat abschalten

score = 0
direction = "down"

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()


canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")#Breite*Höhe+X+Y = Breite in Pixeln mal Höhe in Pixeln plus Abstand vom linken Rand(px) + Abstand vom oberen Rand(px)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()