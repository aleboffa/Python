import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()
a = 30
b = 380-robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

to_der = False
to_izq = False
to_arr = False
to_aba = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_a:
                to_izq = True
            if event.key == pygame.K_d:
                to_der = True
            if event.key == pygame.K_w:
                to_arr = True
            if event.key == pygame.K_s:
                to_aba = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_a:
                to_izq = False
            if event.key == pygame.K_d:
                to_der = False
            if event.key == pygame.K_w:
                to_arr = False
            if event.key == pygame.K_s:
                to_aba = False

        if event.type == pygame.QUIT:
            exit()
# player 1
    if to_right and x <= 590:
        x += 2
    if to_left and x >= 0:
        x -= 2
    if to_up and y >= 0:
        y -= 2
    if to_down and y <= 390:
        y += 2

# player 2
    if to_der and a <= 590:
        a += 2
    if to_izq and a >= 0:
        a -= 2
    if to_arr and b >= 0:
        b -= 2
    if to_aba and b <= 390:
        b += 2
    #######################    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y)) # player 1
    window.blit(robot, (a, b)) # player 2
    pygame.display.flip()

    clock.tick(60)
##########################################
##  solucion del profesor
###########
#
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# # positions of robots
# positions = [[0, 0],
#           [width-robot.get_width(), height-robot.get_height()]]
 
# controls = []
# # key, which robot moves, horizontal movement, vertical movement
# controls.append((pygame.K_LEFT, 0, -2, 0))
# controls.append((pygame.K_RIGHT, 0, 2, 0))
# controls.append((pygame.K_UP, 0, 0, -2))
# controls.append((pygame.K_DOWN, 0, 0, 2))
# controls.append((pygame.K_a, 1, -2, 0))
# controls.append((pygame.K_d, 1, 2, 0))
# controls.append((pygame.K_w, 1, 0, -2))
# controls.append((pygame.K_s, 1, 0, 2))
 
# clock = pygame.time.Clock()
 
# key_pressed = {}
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             key_pressed[event.key] = True
 
#         if event.type == pygame.KEYUP:
#             del key_pressed[event.key]
 
#         if event.type == pygame.QUIT:
#             exit()
 
#     for key in controls:
#         if key[0] in key_pressed:
#             positions[key[1]][0] += key[2]
#             positions[key[1]][1] += key[3]
 
#     screen.fill((0, 0, 0))
#     for i in range(2):
#         screen.blit(robot, (positions[i][0], positions[i][1]))
#     pygame.display.flip()
 
#     clock.tick(60)
