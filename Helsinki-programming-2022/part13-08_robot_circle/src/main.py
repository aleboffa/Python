import pygame
import math

def posicion(x,y,angle):
    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2
    return (x,y)


pygame.init()
window = pygame.display.set_mode((640, 480))
angle = 0

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()
x = 320+math.cos(angle)*100-robot.get_width()/2
y = 240+math.sin(angle)*100-robot.get_height()/2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, posicion(x, y, angle))
    window.blit(robot, posicion(x, y, angle+0.75))
    window.blit(robot, posicion(x, y, angle+1.5))
    window.blit(robot, posicion(x, y, angle+2.25))
    window.blit(robot, posicion(x, y, angle+3))
    window.blit(robot, posicion(x, y, angle+3.75))
    window.blit(robot, posicion(x, y, angle+4.5))
    window.blit(robot, posicion(x, y, angle+5.25))
    window.blit(robot, posicion(x, y, angle+6))
    window.blit(robot, posicion(x, y, angle+6.75))

    pygame.display.flip()

    angle += 0.01

    clock.tick(60)

################################
## solucion profesor
# ##
# import pygame
# import math
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# angle = 0
# radius = 150
# number = 10
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     screen.fill((0, 0, 0))
#     for i in range(number):
#         x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
#         y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
#         screen.blit(robot, (x, y))
#     pygame.display.flip()
 
#     angle += 0.01
#     clock.tick(60)