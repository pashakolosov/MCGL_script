import pyautogui as pg
import time


duration = 0
increase = 35


cell_1 = {
    'x': 1215,
    'y': 690
}

profCraft_cell_4 = {
    'x': 1325,
    'y': 735
}

profCraft_result = {
    'x': 1400,
    'y': 735
}


print('Начало работы скрипта через 5 сек')
time.sleep(5)
# ===========================================================================


def take_a_bucket_of_lava():
    pg.moveTo(cell_1['x'], cell_1['y'], duration=duration)
    pg.click()


def drag_the_bucket():
    pg.moveTo(profCraft_cell_4['x'], profCraft_cell_4['y'], duration=duration)
    pg.click()


def pick_up_steel_through_shift():
    pg.moveTo(profCraft_result['x'], profCraft_result['y'], duration=duration)
    pg.keyDown('shift')
    pg.click()
    pg.keyUp('shift')


def craft_steel():
    take_a_bucket_of_lava()
    drag_the_bucket()
    pick_up_steel_through_shift()
    cell_1['x'] += increase


def craft_27_steel():
    index = 0

    while index < 27:

        if index % 9 == 0:
            cell_1['x'] = 1215
            cell_1['y'] -= increase

        craft_steel()
        index += 1
















