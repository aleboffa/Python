import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1

clock = pygame.time.Clock()

arriba = True
derecha = False
abajo = False
izq = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if arriba:
        window.blit(robot, (x, y))
        x += velocity
    elif derecha:
        window.blit(robot, (x, y))
        y += velocity
    elif abajo:
        window.blit(robot, (x, y))
        x -= velocity
    elif izq:
        window.blit(robot, (x, y))
        y -= velocity

        
    pygame.display.flip()

    if arriba and x+robot.get_width() >= 640: # llego arriba derecha y cambia hacia abajo derecha
        arriba = False
        derecha = True  # va por derech hacia abajo
        abajo = False
        izq = False

        x = 590
        y = 1

    if derecha and y+robot.get_height() >= 480: # llego abajo derecha y cambia abajo hacia izq
        arriba = False
        derecha = False
        abajo = True   # va por abajo hacia izq
        izq = False
        
        x = 590
        y = 390

    if abajo and x+robot.get_width() <= 50: # llego abajo izq y cambia hacia arriba izq
        arriba = False
        derecha = False
        abajo = False
        izq = True  # va por izq hacia arriba

        x = 0
        y = 390

    if izq and y+robot.get_height() <= 80: # llego arriba derecha y cambia hacia abajo derecha
        arriba = True  # va por arriva hacia derecha
        derecha = False
        abajo = False
        izq = False

        x = 0
        y = 0

    clock.tick(120)

    ####################################
    #   solucion profesor
    ################
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# x = 0
# y = 0
# direction = 1 # 1 = to right, 2 = to down, 3 = to left, 4 = to up
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x, y))
#     pygame.display.flip()
 
#     if direction == 1:
#         x += 1
#         if x+robot.get_width() == width:
#             direction = 2
#     elif direction == 2:
#         y += 1
#         if y+robot.get_height() == height:
#             direction = 3
#     elif direction == 3:
#         x -= 1
#         if x == 0:
#             direction = 4
#     elif direction == 4:
#         y -= 1
#         if y == 0:
#             direction = 1
 
#     clock.tick(60)
# # # WRITE YOUR SOLUTIO
