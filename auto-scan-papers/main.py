from functions import *

# Abre la aplicación Paint
pyautogui.press('win')  # Abre el menú Inicio (puede variar según tu sistema operativo)
pyautogui.write('Paint')  # Escribe "Paint" para buscar la aplicación
pyautogui.press('enter')  # Abre Paint

scan_file()
