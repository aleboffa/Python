import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
despl = 30
for y in range(10):
    for x in range(10):
        screen.blit(robot, (despl+50*x, 70+30*y))
    despl += 10
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


####################################
#### solucion profesor

# screen.fill((0, 0, 0))
# for i in range(10):
#     for j in range(10):
#         screen.blit(robot, (20+10*i+40*j, 100+i*20))
# pygame.display.flip()
 