import numpy as np
import pyautogui
import cv2
from PIL import ImageGrab
import time
import keyboard

# Get and Set the screen size
screen_width, screen_height = pyautogui.size()

# The video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Create object to save the video
save_video = cv2.VideoWriter("Screen_recording.avi", fourcc, 20, (screen_width, screen_height))

print("Recording started. Press ESC to stop the recording.")

# Start recording

while True:
    # capture the screen using pillow ImageGrab
    image = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    frame = np.array(image)

    # Convert the color from RGB to BDR (OpenCV accept BDR)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to video
    save_video.write(frame)

    # Recording will stop when the user presses ESC.
    if keyboard.is_pressed('esc'):
        print("Recording stopped.")
        break

# Release Video Writer
save_video.release()

# Close all window
cv2.destroyAllWindows()

print("Screen record saved.")