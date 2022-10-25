import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 100
a = 0
b = 200
velocity_x = 1
velocity_a = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (a, b))
    pygame.display.flip()

#   robot 1    
    x += velocity_x
    if velocity_x > 0 and x+robot.get_width() >= 640:
        velocity_x = -velocity_x
    if velocity_x < 0 and x <= 0:
        velocity_x = -velocity_x

#   robot 2
    a += velocity_a
    if velocity_a > 0 and a+robot.get_width() >= 640:
        velocity_a = -velocity_a
    if velocity_a < 0 and a <= 0:
        velocity_a = -velocity_a

    clock.tick(60)

#############################################
######   solucion del profesor
#
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# x1 = 0
# x2 = 0
# speed1 = 1
# speed2 = 2
 
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     x1 += speed1
#     if x1 == 0 or x1+robot.get_width() == width:
#         speed1 = -speed1
#     x2 += speed2
#     if x2 == 0 or x2+robot.get_width() == width:
#         speed2 = -speed2
 
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x1, 50))
#     screen.blit(robot, (x2, 200))
#     pygame.display.flip()
 
#     clock.tick(60)
