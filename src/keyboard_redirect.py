import pyautogui

def redirect_input(gaze_direction, key):
    if gaze_direction == 'left':
        pyautogui.hotkey('win', 'left')
    elif gaze_direction == 'right':
        pyautogui.hotkey('win', 'right')
