# WRITE YOUR SOLUTION HERE:
import pygame
import random

print(random.randrange(3, 9))
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
ancho=600
alto=400

screen.fill((0, 0, 0))
for i in range(100):
    x=random.randrange(0, ancho)
    for j in range(10):
        y=random.randrange(0, alto)
        screen.blit(robot, (x,y))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
####################################
######  solucion profesor
###
# import pygame
# from random import randint
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((640, 480))
 
# robot = pygame.image.load("robot.png")
 
# screen.fill((0, 0, 0))
# for i in range(1000):
#     x = randint(0,width-robot.get_width())
#     y = randint(0,height-robot.get_height())
#     screen.blit(robot, (x,y))
# pygame.display.flip()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()