# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("by Alex Boffa-2022")
 
def circle(color: int, radius: int):
    pygame.draw.circle(screen, color, (middle_x, middle_y), radius)
 
def hand(length: int, thickness: int, proportion: float): # define las agujas del reloj
    angle = 2*math.pi*proportion-math.pi/2
    end_x = middle_x+math.cos(angle)*length
    end_y = middle_y+math.sin(angle)*length
 
    pygame.draw.line(screen, (0, 0, 255), (middle_x, middle_y), (end_x, end_y), thickness)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    hours = datetime.now().hour%12
    minutes = datetime.now().minute
    seconds = datetime.now().second
 
    pygame.display.set_caption(str(datetime.now().time())[:8]) # toma la hora completa del sistema en formato HH:MM:SS(8 CHAR)
 
    screen.fill((0, 0, 0)) # pinta la pantallita de negro
    
    # centro de la pantalla
    middle_x = width/2  
    middle_y = height/2
 
    circle((255, 0, 0), 200) # circulo relleno rojo
    circle((0, 0, 0), 195) # circulo relleno negro para tapar parte del rojo
    circle((255, 0, 0), 10) # circulo relleno rojo pequeño del centro del reloj
 
    hand(185, 1, seconds/60)     # aguja segundos
    hand(180, 2, (minutes+seconds/60)/60)  # aguja minutos
    hand(150, 5, (hours+minutes/60+seconds/3600)/12) # aguja horas
 
    pygame.display.flip()