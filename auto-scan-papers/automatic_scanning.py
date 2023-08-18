from functions import *

# Open Paint app
pyautogui.press('win')
pyautogui.write('Paint')
pyautogui.press('enter')

# Calls the scan_file function, which is in charge of automatic scanning
scan_file()
