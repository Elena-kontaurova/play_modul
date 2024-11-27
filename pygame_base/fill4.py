''' Код с использованием с
рисуем четырехугольник'''
import pygame

screen = pygame.display.set_mode((600, 400))
pygame.display.update()

fps = 60
clock = pygame.time.Clock()

start_pos = None

while True:
    screen.fill((255, 255, 255))

    if pygame.mouse.get_pressed()[0]:
        if start_pos is None:
            start_pos = pygame.mouse.get_pos()

    if start_pos is not None:
        end_pos = pygame.mouse.get_pos()
        width = end_pos[0] - start_pos[0]
        hight = end_pos[1] - start_pos[1]
        pygame.draw.rect(screen, (0, 255, 255),
                         (start_pos[0], end_pos[1], width, hight))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            start_pos = None

    clock.tick(fps)
    pygame.display.update()
