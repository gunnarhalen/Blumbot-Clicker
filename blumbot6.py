import pyautogui
import pygetwindow as gw
import time
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
░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░  
  by Peralta   
    """)

anjaymabar()
print()
print(":::::::::::::::::::: ESCOLHA A JANELA DO TELEGRAM COM BLUM ::::::::::::::::::::")

window_input = f"Choose Window (1 - TelegramDesktop): "
window_not_found = f"Janela {{}} não encontrada!"
window_found = f"Janela encontrada: {{}}\n Iniciando bot... Aperte 'K' no teclado para pausar/reiniciar o Blumbot."
pause_message = f"Blumbot pausado... Aperte 'K' novamente para continuar."
continue_message = f"Blumbot reiniciado..."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def locate_button(template_path, threshold=0.8):
    template = cv2.imread(template_path)
    template_height, template_width, _ = template.shape

    scrn = pyautogui.screenshot()
    scrn_np = np.array(scrn)
    scrn_np = cv2.cvtColor(scrn_np, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(scrn_np, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        for pt in zip(*loc[::-1]):
            click(pt[0] + template_width // 2, pt[1] + template_height // 2)
            pyautogui.moveTo(0, 0)  # Mover o mouse para fora da janela
            return True

    return False

def scroll_window(window_rect):
    center_x = window_rect[0] + window_rect[2] // 2
    center_y = window_rect[1] + window_rect[3] // 2
    mouse.position = (center_x, center_y)
    
    for _ in range(5):
        pyautogui.scroll(-100, x=center_x, y=center_y)
        time.sleep(0.2)

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False
    button_clicked = False
    last_color_found_time = time.time()

    while True:
        if keyboard.is_pressed('K'):
            paused = not paused
            print(pause_message if paused else continue_message)
            time.sleep(0.2)

        if paused:
            continue

        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

        window_rect = (telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height)

        # Rola a janela e tenta localizar o botão Play
        if not button_clicked:
            scroll_window(window_rect)

            if locate_button('images/playButton.png'):
                print("Iniciando jogo.")
                button_clicked = True
            else:
                print("Botão não encontrado. Aguardando...")
                continue

        # Loop de jogar clicando nas cores
        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))
        width, height = scrn.size
        pixel_found = False

        # LEMBRETE: Testar range com valor 10 para aumento do performance na identificação das cores. Pode aumentar uso de CPU.
        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = scrn.getpixel((x, y))
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    last_color_found_time = time.time()
                    # LEMBRETE: Testar time.sleep(0.0001) para evitar clique errado na bomba
                    time.sleep(0.001) 
                    pixel_found = True
                    break

        # Se passaram mais de 3 segundos sem encontrar cor, reinicia o jogo
        if not pixel_found and (time.time() - last_color_found_time > 3):
            print("Fim de partida. Reiniciando jogo.")
            
            if locate_button('images/playAgainButton.png', threshold=0.6):
                print("'Jogando novamente'.")
                button_clicked = True  # Continua jogando após clicar no "Play Again"
                last_color_found_time = time.time()
                time.sleep(1)  # Pequeno atraso para garantir que o jogo reinicie
            else:
                print("Sem fichas restantes. Encerrando o Blumbot...")
                break  # Encerra o loop se o botão não for encontrado
