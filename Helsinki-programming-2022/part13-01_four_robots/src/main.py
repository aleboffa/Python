
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
window.blit(robot, (0, 0))
window.blit(robot, (590, 0))
window.blit(robot, (590, 390))
window.blit(robot, (0, 390))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

##########################################
### solucion profesor ##########
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# right_x = width-robot.get_width()
# down_y = height-robot.get_height()
 
# screen.fill((0, 0, 0))
# screen.blit(robot, (0, 0))
# screen.blit(robot, (right_x, 0))
# screen.blit(robot, (0, down_y))
# screen.blit(robot, (right_x, down_y))
# pygame.display.flip()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 