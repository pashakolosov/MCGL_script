import pyautogui as pg
import time


print('start after 10 sec')
time.sleep(10)

while True:
    print(pg.position())
    time.sleep(0.5)
