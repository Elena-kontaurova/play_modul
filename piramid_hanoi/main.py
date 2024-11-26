''' Реализация игры Ханойские башни на Python'''
import sys

import pygame


pygame.init()


WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
RED_COLOR = (0, 0, 0)
DISK_COLORS = [(255, 0, 0, ), (0, 255, 0), (0, 0, 255),
               (255, 255, 0), (255, 165, 0), (128, 0, 128)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ханойские башни')


class Disk:
    ''' Класс диска содержит атрибуты ширины, высоты и цвета диска,
    а также прямоугольник для отрисовки'''
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(0, 0, width, height)


class Peg:
    ''' Позиция и список дисков
    Методы для добавления и удаления дисков'''
    def __init__(self, x):
        self.x = x
        self.disks = []

    def add_disk(self, disk):
        ''' метод добавления диска'''
        self.disks.append(disk)

    def remove_disk(self):
        ''' Метод удаления диска'''
        return self.disks.pop() if self.disks else None

    def top_disk(self):
        ''' Метод, который возвращает верхний диск'''
        return self.disks[-1] if self.disks else None


def draw_pegs(pegs):
    ''' Функция отрисовки стержней и дисков'''
    for peg in pegs:
        pygame.draw.rect(screen, RED_COLOR, (peg.x, HEIGHT - 40, 10, 80))
        for i, disk in enumerate(peg.disks):
            disk.rect.x = peg.x - disk.width // 2 + 5
            disk.rect.y = HEIGHT - 40 - (i - 1) * disk.height
            pygame.draw.rect(screen, disk.color, disk.rect)


def main():
    ''' d'''
    pegs = [Peg(200), Peg(300), Peg(400)]
    num_disks = 4
    for i in range(num_disks - 1, -1, -1):
        disk = Disk(50 + i * 20, 20, DISK_COLORS[i % len(DISK_COLORS)])
        pegs[0].add_disk(disk)

    selected_disk = None
    selected_peg_index = None

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_pegs(pegs)

        if len(pegs[2].disks) == num_disks:
            print('Вы выйграли!!!')
            font = pygame.font.Font(None, 74)
            text = font.render("Вы выйграли!!!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, _ = event.pos
                for i, peg in enumerate(pegs):
                    if peg.x - 30 < mouse_x < peg.x + 30:
                        if selected_disk is None:
                            selected_disk = peg.top_disk()
                            if selected_disk:
                                selected_peg_index = i
                        else:
                            top_disk = peg.top_disk()
                            if selected_disk and (top_disk is None or
                                                  (isinstance(top_disk, Disk)
                                                   and selected_disk.width
                                                   < top_disk.width)):
                                peg.add_disk(selected_disk)
                                # Проверяем, что selected_peg_index установлен
                                if selected_peg_index is not None:
                                    removed_disk = pegs[
                                        selected_peg_index].remove_disk()
                                    if removed_disk is None:
                                        print("Ошибка: нет дисков для \
                                              удаления с выбранного стержня.")
                                else:
                                    print("Ошибка: выбранный индекс \
                                          стержня не установлен.")
                            selected_disk = None

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
