import pygame
from pygame.locals import *
import sys

# pygame initialization
pygame.init()
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))   
clock = pygame.time.Clock()

w = 200
h = 100

dt = 0

dvd = pygame.math.Vector2(100, 100)
logo_vector = pygame.math.Vector2(dvd.x-40, dvd.y-40)
vel = pygame.math.Vector2(10, 10)

logo_img = pygame.image.load("logo.png")

# game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill("white")

    dvd.x += vel.x * dt
    dvd.y += vel.y * dt

    if (dvd.x+88) >= screenWidth or (dvd.x-40) <= 0:
        vel.x *= -1 
    if (dvd.y+40) >= screenHeight or (dvd.y-40) <= 0:
        vel.y *= -1

    screen.blit(logo_img, (dvd.x-40, dvd.y-40))

    pygame.display.flip()
    dt = clock.tick(60) / 30
