# WRITE YOUR SOLUTION HERE:
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
right_x = width-robot.get_width()
down_y = height-robot.get_height()
 
screen.fill((0, 0, 0))
for x in range(50,550,50):
    screen.blit(robot, (x, 100))

pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 