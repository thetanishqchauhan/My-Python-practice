import pyautogui as pg
import time

print("starting in 10 seconds...")
time.sleep(10)

for i in range(1):
    pg.write("Hello!!!")
    pg.press("Enter")
