### Pac-Robot GAME by Alex Boffa-2022

import pygame
import time
from random import randint

####   function Bye() show final points when press X or ESC keys 
def bye(points):    
    font = pygame.font.SysFont("Arial", 60)
    if points >= 0: #   green sign you won 
        text = font.render("You WON "+str(points)+" Points", True, (0,255,0))
    else:   #   red sign you lost
        text = font.render("You LOST "+str(abs(points))+" Points", True, (255,0,0))
    # background color
    screen.fill((0, 0, 0))
    screen.blit(text, (width-650, 250)) # right-up corner
    pygame.display.flip()
    time.sleep(3)   # wait 3 sec
####
#### function check_actors() checks position of coins and monsters
def check_actors(x,positions,number,robot,coin,points,reward):
    for i in range(number):
        positions[i][1] += 1
        if positions[i][1]+coin.get_height() >= y:
            robot_middle = x+robot.get_width()/2
            coin_middle = positions[i][0]+coin.get_width()/2
            if abs(robot_middle-coin_middle) <= (robot.get_width()+coin.get_width())/2:
                # robot catch a coin
                positions[i][0] = randint(0,width-coin.get_width())
                positions[i][1] = -randint(100,1000)
                points += reward # if catch a coin, win 10 points

    return x,points
####
#### check keys pressed
def event_key(x,to_left,to_right,points):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                bye(points) #   show final points when press ESC key
                exit()  #   exit game

        #   enable "X" right-up in windows to quit
        if event.type == pygame.QUIT:   
            bye(points) #   show final points when press X
            exit()  #   exit game

    #   check if key rightor left are pressed and move the robot x pixels
    if to_right and x <= 750:  
        x += 4
    if to_left and x >= 0:
        x -= 4 

    return x,to_left,to_right,points
####

####  start main program
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Robot by Alex Boffa-2022 /// catch a coin, win 10 pts - touch a monster, lose 10 pts /// Press `Esc` to exit")
robot = pygame.image.load("robot.png")    
x = 0
y = height - robot.get_height()
points = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20) 

coin = pygame.image.load("coin.png")    #   coin to catch
monster = pygame.image.load("monster.png")  # monster alien to avoid

number = 10 # number of coins to collect from sky
number_monster = 5 # number of monsters aliens to avoid from sky

positions = []
for i in range(number):
    positions.append([randint(0,width - coin.get_width()),-randint(100,1000)])

positions_monsters = []
for i in range(number_monster):
    positions_monsters.append([randint(0,width - monster.get_width()),-randint(100,1000)])

to_right = False
to_left = False  
  
while True:
    # start event key
    x,to_left,to_right,points = event_key(x,to_left,to_right,points)
    # end event key

    # start check coins
    reward = 10
    x,points = check_actors(x,positions,number,robot,coin,points,reward)
    # end check coins

    # start check monsters
    reward = -10
    x,points = check_actors(x,positions_monsters,number_monster,robot,monster,points,reward)
    # end check monsters

    # window background color
    screen.fill((0, 100, 100))
    # draw robot
    screen.blit(robot, (x, y))
    # draw coins
    for i in range(number):
        screen.blit(coin, (positions[i][0], positions[i][1]))
    # draw monsters
    for i in range(number_monster):
        screen.blit(monster, (positions_monsters[i][0], positions_monsters[i][1]))
    # draw points
    text = font.render("Points: "+str(points), True, (255,255, 0)) #color yellow(255,255,0)
    screen.blit(text, (width-100, 10)) # right-up corner
    # refresh screen
    pygame.display.flip()
    # set velocity of refreshing screen(cycles of program by second)
    clock.tick(120) # draw 120 frames x second
    


