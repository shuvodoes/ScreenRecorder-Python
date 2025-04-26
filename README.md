# Screen Recorder using Python

A high-performance Python screen recording tool leveraging OpenCV and PyAutoGUI for seamless and efficient screen capture.

This project uses:
- `OpenCV` for handling video writing,
- `Pillow` (`ImageGrab`) for screen capturing,
- `PyAutoGUI` for getting screen dimensions,
- `Keyboard` for listening to keypress events.

# Features
- Capture the entire screen.
- Save the recording as an `.avi` file.
- Press **ESC** anytime to stop recording.
- Lightweight and easy to run.

# Requirements

Make sure you have Python installed, then install the necessary libraries:

# How to Run
1. Clone the repository or copy the script.
2. Install the dependencies.
3. Run the script:

```bash
python screen_recorder.py
```

4. Screen recording will start immediately.
5. Press **ESC** key to stop and save the recording.

The output file will be saved as:

```
Screen_recording.avi
```
# Project Structure

screen_recorder/
├── screen_recorder.py
├── Screen_recording.avi (generated after recording)
└── README.md


# Example in Action

> "Recording started. Press ESC to stop the recording."

# Notes

- The recording frame rate is set to **20 FPS**.
- The video codec used is **XVID** (`.avi` format).
- Works on **Windows** (since `ImageGrab` is fully supported). For Linux/Mac, small modifications might be needed.


# Future Improvements

- Add GUI interface for starting and stopping recording.
- Allow custom screen area selection.
- Save videos in multiple formats (e.g., `.mp4`).
- Add sound recording (microphone + system audio).

# Contribution

Feel free to fork, improve, and create pull requests!  
If you find any bugs or have suggestions, feel free to open an issue.

# License

This project is open-source and available under the [MIT License](LICENSE).


