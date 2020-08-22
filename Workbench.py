import pyautogui as pg
import time

duration = 0
increase = 35

cell_1 = {
    'x': 1300,
    'y': 745
}
cellCraft = {
    'x': 1545,
    'y': 460
}

print('Начало работы скрипта через 5 сек')
time.sleep(5)
# ===========================================================================


def click_on_the_first_cell():
    pg.moveTo(cell_1['x'], cell_1['y'], duration=duration)
    pg.click()


def click_on_the_last_cell():
    pg.moveTo(cellCraft['x'], cellCraft['y'], duration=duration)
    pg.click()


def combo_switch():

    pg.keyDown('shift')

    index = 0

    while index < 32:

        if index % 9 == 0:
            cell_1['x'] = 1300
            cell_1['y'] -= increase

        click_on_the_first_cell()
        click_on_the_last_cell()

        index += 1
        cell_1['x'] += increase

    pg.keyUp('shift')


if __name__ == '__main__':
    combo_switch()