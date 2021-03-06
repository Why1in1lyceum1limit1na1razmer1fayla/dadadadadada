import pygame
import sys
import os
import requests

map_file = 'map.png'


def gm(ln, lt, m):
    global map_file
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={ln},{lt}&spn={m},{str(float(m) / 2)}&l=map"
    response = requests.get(map_request)
    if str(response) != '<Response [404]>':
        print('OK')
        with open(map_file, 'wb') as file:
            file.write(response.content)
    else:
        print('Error')


pygame.init()
pygame.display.set_caption('Maps api')
size = 500, 450
screen = pygame.display.set_mode(size)
running = True
lnn = input('Введите долгота: ')
ltt = input('Введите широта: ')
mm = input('Введите масштаб 0-17: ')
gm(lnn, ltt, mm)
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (float(ltt) + float(mm) < 90):
                ltt = str(float(ltt) + 0.1 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_DOWN and (float(ltt) - float(mm) > -90):
                ltt = str(float(ltt) - 0.1 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_LEFT and (float(ltt) + float(mm) < 180):
                lnn = str(float(lnn) - 0.25 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_RIGHT and (float(ltt) - float(mm) > -180):
                lnn = str(float(lnn) + 0.25 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_PAGEUP and (float(mm) < 175):
                mm = str(float(mm) + 2.5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_PAGEDOWN and (float(mm) > 2.5):
                mm = str(float(mm) - 2.5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

    # screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()
