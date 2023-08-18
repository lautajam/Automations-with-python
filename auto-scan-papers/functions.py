import pyautogui
import time
import pyautogui

# Possed the mouse and click the button
def put_mouse_click(pos_x, pos_y, button_touched):

    time.sleep(0.5) 

    pyautogui.click(x= pos_x, y= pos_y)

    # print("Button '" + button_touched + "' selected.") For debug

def scan_file():
    """
    This function simulates a series of mouse clicks to navigate through a scanning process.
    It moves the mouse cursor to specific positions and clicks on various elements on the screen.
    The purpose of the function is to automate the scanning process in a specific application.

    Steps:
    1. Move the cursor to initial position.
    2. Click on 'Files' button.
    3. Click on 'Scanner' option.
    4. Click on 'White/Black file' option.
    5. Click on 'Digitalizate' button.
    6. Move the cursor back to the initial position.
    7. Wait for 10 seconds.
    8. Click on 'Files' button again.
    9. Click on 'Save' option.

    Note: This function assumes that the screen resolution and the positions of UI elements
    on the screen remain constant. Adjust the coordinates if needed.
    
    """
    
    pyautogui.moveTo(x=500, y=10)

    put_mouse_click(30, 30, 'Files')

    put_mouse_click(230, 290, 'Scanner')

    put_mouse_click(800, 540, 'White/Black file')

    put_mouse_click(1100, 700, 'Digitalizate')

    pyautogui.moveTo(x=500, y=10)

    time.sleep(10) # This time may change, depending on your PC, the file to be scanned, etc.

    put_mouse_click(30, 30, 'Files')

    put_mouse_click(230, 190, 'Save')
    
