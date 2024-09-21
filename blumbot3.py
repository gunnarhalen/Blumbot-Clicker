import pyautogui
import pygetwindow as gw
import time
from termcolor import colored
import keyboard
import random
from pynput.mouse import Button, Controller
import cv2
import numpy as np

mouse = Controller()
time.sleep(0.5)

def anjaymabar():
    print(f"""

░▒▓███████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓██████████████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░     
    """)

anjaymabar()
print()
print(":::::::::::::::::::: CHOOSE TELEGRAM LANGUAGE ::::::::::::::::::::")
print("ENGLISH SELECTED BY DEFAULT")

window_input = f"Choose Window (1 - TelegramDesktop): "
window_not_found = f"Your Window - {{}} not found!"
window_found = f"Window found - {{}}\n Bot working... Press 'K' on the keyboard to pause."
pause_message = f"Bot paused... Press 'K' again on the keyboard to continue."
continue_message = f"Bot continue working..."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def locate_button(template_path):
    template = cv2.imread(template_path)
    template_height, template_width, _ = template.shape

    scrn = pyautogui.screenshot()
    scrn_np = np.array(scrn)
    scrn_np = cv2.cvtColor(scrn_np, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(scrn_np, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        for pt in zip(*loc[::-1]):
            click(pt[0] + template_width // 2, pt[1] + template_height // 2)
            return True

    return False

def scroll_window(window_rect):
    # Move o mouse para o centro da janela antes de rolar
    center_x = window_rect[0] + window_rect[2] // 2
    center_y = window_rect[1] + window_rect[3] // 2
    mouse.position = (center_x, center_y)
    
    for _ in range(5):  # Ajuste o número de rolagens conforme necessário
        pyautogui.scroll(-100, x=center_x, y=center_y)
        time.sleep(0.2)

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

if window_name == '2':
    window_name = "KotatogramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
    print(f"EN: Make sure you use the TelegramDesktop application (not Telegram Web). And have opened the Blum bot on your TelegramDesktop. Until the Blum window is available.")
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False

    while True:
        if keyboard.is_pressed('K'):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)

        if paused:
            continue

        # Tente ativar a janela do Telegram
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        )

        # Rola a janela para trazer o botão para a vista
        scroll_window(window_rect)

        # Localiza o botão antes de identificar cores
        if not locate_button('images/playButton.png'):
            print("Botão não encontrado. Aguardando...")
            continue

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size
        pixel_found = False
        if pixel_found:
            break

        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = scrn.getpixel((x, y))
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break
