import time
import pyautogui as pg

print("programa rodando…")
time.sleep(0.1)

for i in range(20):
    pg.write(" Boa Noite ")
    time.sleep(0.1)
    pg.press("Enter")
