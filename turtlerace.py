import turtle
import time
import random
from os import system, name # Import the system and name module

#Size of the Screen
WIDTH, HEIGHT = 500, 500

#Turtle Colors
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def clear(): # Function to clean screen
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear') 


#Function to select the number of turtles for the race with print msg in case not a valid number and choose the turtle to win the race
def get_number_of_racers():

    racers = 0
    
    while True:
        racers = input('Enter the number of Turtles (2-10): ')
        if racers.isdigit():
            global colors
            global turtleplayer
            racers = int(racers)
            random.shuffle(COLORS)
            colors = COLORS[:racers]
        
        else:
            print('\nInput is not numeric... Try Again!\n')
            continue

        if 2 <= racers <= 10:
            turtleplayer = ""
            while turtleplayer not in colors:
                print('\nTurtles:', colors)
                turtleplayer = input('\nPlease choose one available Turtle: ')
            return racers
        else:
            print('\nNumber not in range 2-10. Try Again!\n')  
       

#Function to define the speed of the turtles
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


#Function to set turtles position
def create_turtles(colors):
    turtles =[]
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

#Screen Function Setup
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

#Initiate 'get_number_of_racers' and 'init_turtle' functions
clear()
racers = get_number_of_racers()
init_turtle()


winner = race(colors)

if winner == turtleplayer:
    print('\nCongratulations! Your', winner.capitalize(), 'Turtle Won the Race.')
else:
    print('\nYou lost!', winner.capitalize(), 'Turtle Won the Race')

time.sleep(5)
