# Banana Auto Clicker

The Banana Auto Clicker is a Python-based application that allows users to automate mouse clicks at specific locations on the screen. This tool can be useful for repetitive tasks, such as playing games or performing other routine actions that require frequent clicking.

## Features

1. **Add Point**: The user can click the "Add Point" button to mark a location on the screen where the auto clicker will perform a click.
2. **Start Clicking**: The user can start the auto clicking process by clicking the "Start Clicking" button. The program will then click at each of the marked locations, with a customizable delay between each click.
3. **Stop Clicking**: The user can stop the auto clicking process by clicking the "Stop Clicking" button or by pressing the Esc key.
4. **Save Locations**: The program automatically saves the locations of the marked points in a file named "locations.txt" when the application is closed.

## Requirements

The Banana Auto Clicker requires the following Python libraries:

- `win32api`
- `win32con`
- `time`
- `tkinter`
- `pynput`

These libraries can be installed using pip:

```
pip install pywin32 pynput
```

## Usage

1. Run the Python script.
2. Click the "Add Point" button to mark the locations where you want the auto clicker to perform clicks.
3. Adjust the "Click Speed" entry to set the delay between each click (in seconds).
4. Click the "Start Clicking" button to begin the auto clicking process.
5. To stop the auto clicking, click the "Stop Clicking" button or press the Esc key.
6. The program will automatically save the marked locations in the "locations.txt" file when you close the application.

## Disclaimer

This tool is intended for personal use and should be used responsibly. The developer is not responsible for any misuse or consequences arising from the use of this application.
