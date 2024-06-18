import pyautogui

def redirect_input(gaze_direction, key):
    if gaze_direction == 'left':
        pyautogui.click(x=0, y=0)
    elif gaze_direction == 'right':
        pyautogui.click(x=-2400, y=0)
