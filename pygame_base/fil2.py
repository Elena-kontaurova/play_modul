''' Перемещение прямоугольника с помощью клавиш'''
import pygame

pygame.init()

width = 700
height = 500

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

fps = 60
clock = pygame.time.Clock()

x = width // 2
y = height // 2
speed = 5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed

    screen.fill(white)
    pygame.draw.rect(screen, blue, (x, y, 10, 20))
    pygame.display.update()

clock.tick(fps)
