import pyautogui as pg
import time

pg.PAUSE = 0.1

duration = 0
increase = 35


cell_1 = {
    'x': 1215,
    'y': 735
}

cell_27 = {
    'x': 1500,
    'y': 615
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


def select_the_first_cell():
    pg.moveTo(cell_1['x'], cell_1['y'], duration=duration)
    pg.click()


def put_the_bucket_in_the_craft():
    pg.moveTo(profCraft_cell_4['x'], profCraft_cell_4['y'], duration=duration)
    pg.click()


def pick_up_steel_through_shift():
    pg.moveTo(profCraft_result['x'], profCraft_result['y'], duration=duration)
    pg.keyDown('shift')
    pg.click()
    pg.keyUp('shift')


def craft_steel_one_iteration():
    select_the_first_cell()
    put_the_bucket_in_the_craft()
    pick_up_steel_through_shift()
    cell_1['x'] += increase


def put_the_bucket_in_18_cell():
    put_the_bucket_in_the_craft()
    pg.moveTo(cell_27['x'], cell_27['y'])
    pg.click()


def craft_27_steel():
    index = 0

    while index < 27:

        if index % 9 == 0:
            cell_1['x'] = 1215
            cell_1['y'] -= increase

        craft_steel_one_iteration()
        index += 1

    put_the_bucket_in_18_cell()


def click_on_all_bucket():
    pg.keyDown('shift')

    cell_1['y'] += 105

    index = 0

    while index < 27:

        if index % 9 == 0:
            cell_1['x'] = 1215
            cell_1['y'] -= increase

        select_the_first_cell()
        cell_1['x'] += increase
        index += 1

    pg.keyUp('shift')


if __name__ == '__main__':
    craft_27_steel()

    click_on_all_bucket()












