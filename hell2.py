import pyautogui as pg
import time


duration = 0

index = 0

vedro_pos_x = 1325
vedro_pos_y = 735

first_vedro_x = 1215
first_vedro_y = 690

result_pos_x = 1400
result_pos_y = 735

print('Начало работы скрипта через 5 сек')
time.sleep(5)


def out():
    pg.moveTo(result_pos_x, result_pos_y, duration=duration)
    pg.keyDown('shift')
    pg.click()
    pg.keyUp('shift')


def move_to_craft():
    pg.moveTo(vedro_pos_x, vedro_pos_y, duration=duration)
    pg.click()


move_to_one_line()


while index < 27:
    pg.moveTo(first_vedro_x, first_vedro_y, duration=duration)
    pg.click()
    move_to_craft()
    out()
    first_vedro_x += 35
    index += 1
    if index == 9:
        first_vedro_x = 1215
        first_vedro_y -= 35

    if index == 18:
        first_vedro_x = 1215
        first_vedro_y -= 35
