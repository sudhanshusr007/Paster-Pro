import pyautogui as pg
import time
f = open('text.txt', 'r')
content = f.read()
content = content.replace("  ", "")
time.sleep(7)
pg.write(content)
pg.press("enter")
