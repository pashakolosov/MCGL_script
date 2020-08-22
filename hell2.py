import pyautogui as pg
import time


duration = 0
index = 0


prof_craft_last_cell = {
    'x': 1325,
    'y': 735
}

cell_1 = {
    'x': 1215,
    'y': 690
}

prof_craft_result = {
    'x': 1400,
    'y': 735
}


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


def move_to_one_line(pos1, pos2):
    pg.moveTo(pos1, pos2, duration=duration)
    pg.click()
    move_to_craft()
    out()
    first_vedro_x += 35
    index += 1


while index < 27:
    pg.moveTo(pos_x_1, pos_y_2, duration=duration)
    pg.click()
    move_to_craft()
    out()
    pos_x_1 += 35
    index += 1
    if index == 9:
        pos_x_1 = 1215
        pos_y_2 -= 35

    if index == 18:
        pos_x_1 = 1215
        pos_y_2 -= 35
