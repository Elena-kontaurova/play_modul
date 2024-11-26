''' рисование графических приметивов'''
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
gray = (128, 128, 128)

# Прямоугольник бех границ
pygame.draw.rect(screen, yellow, (10, 10, 50, 100))

# Прямоульгьник с границыми
pygame.draw.rect(screen, purple, (100, 10, 50, 100), 2)

# Нарисовать линию
pygame.draw.line(screen, orange, (200, 20), (350, 50))

# Нарисовать сглаженную линию
pygame.draw.aaline(screen, orange, (200, 40), (350, 70))

# Нарисовать многоугольник
pygame.draw.lines(screen, gray, True, [(200, 80), (250, 80), (300, 200)], 2)

# Нарисовать сглаженный мноугольник
pygame.draw.aalines(screen, gray, True, [(300, 80), (350, 80), (400, 200)], 2)

# Нарисовать замкнутый многоугольник
pygame.draw.polygon(screen, yellow,
                    [[150, 210], [180, 250], [90, 290], [30, 230]])

# Нарисовать замкнутый многоугольник с границей
pygame.draw.polygon(screen, yellow,
                    [[150, 310], [180, 350], [90, 390], [30, 310]], 1)

# Нарисовать окружность
pygame.draw.circle(screen, purple, (300, 250), 40)

# Нарисовать эллипс
pygame.draw.ellipse(screen, purple, (300, 300, 100, 50), 1)

# Нарисовать дугу
pi = 3.14
pygame.draw.arc(screen, gray, (450, 30, 50, 150), pi, 2*pi, 5)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
