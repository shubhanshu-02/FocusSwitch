import cv2
from pynput import keyboard
from face_eye_detection import detect_faces_and_eyes
from gaze_detection import determine_gaze_direction
from keyboard_redirect import redirect_input

gaze_direction = 'center'

def on_press(key):
    global gaze_direction
    redirect_input(gaze_direction, key)
    try:
        print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    left_eye, right_eye = detect_faces_and_eyes(frame)
    if left_eye and right_eye:
        gaze_direction = determine_gaze_direction(left_eye, right_eye)
        print(f'Gaze Direction: {gaze_direction}')
        
        for (x, y) in left_eye:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
        for (x, y) in right_eye:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
