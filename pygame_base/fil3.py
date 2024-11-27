''' Программа по отрисовку прямоугольника'''
import pygame

screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))
pygame.display.update()

fps = 60
clock = pygame.time.Clock()

start_pos = None
end_pos = None
is_drawing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if is_drawing:
                end_pos = event.pos
                screen.fill((255, 255, 255))
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                pygame.draw.rect(screen, (0, 255, 255),
                                 (start_pos[0], start_pos[1], width, height))
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False
            screen.fill((255, 255, 255))
            pygame.display.update()

    clock.tick(fps)
