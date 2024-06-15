import win32api
import win32con
import time
import tkinter as tk
from pynput import keyboard

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def mark_click(x, y):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

def add_point():
    window.withdraw()  # Hide the main window
    time.sleep(1)  # Wait for 1 second
    x, y = win32api.GetCursorPos()  # Get the current cursor position
    window.deiconify()  # Show the main window again
    points.append((x, y))
    listbox.insert(tk.END, f"({x}, {y})")
    mark_click(x, y)

def start_clicking():
    global running, listener
    running = True
    click_speed = float(speed_entry.get())
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while running:
        for point in points:
            if not running:
                break
            x, y = point
            click(x, y)
            time.sleep(click_speed)  # Delay between each click based on the click speed
    listener.stop()

def stop_clicking():
    global running
    running = False
    save_locations()

def on_press(key):
    if key == keyboard.Key.esc:
        stop_clicking()
        return False

def save_locations():
    with open("locations.txt", "w") as file:
        for x, y in points:
            file.write(f"({x}, {y})\n")

# Create the main window
window = tk.Tk()
window.title("Auto Clicker")

# Create a button to add points
button_add = tk.Button(window, text="Add Point", command=add_point)
button_add.pack()

# Create a listbox to display the added points
listbox = tk.Listbox(window)
listbox.pack()

# Create a canvas to mark the clicked locations
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create a label and entry for click speed
speed_label = tk.Label(window, text="Click Speed (seconds):")
speed_label.pack()
speed_entry = tk.Entry(window)
speed_entry.insert(tk.END, "0.5")  # Default click speed of 0.5 seconds
speed_entry.pack()

# Create a button to start clicking
button_start = tk.Button(window, text="Start Clicking", command=start_clicking)
button_start.pack()

# Create a button to stop clicking
button_stop = tk.Button(window, text="Stop Clicking", command=stop_clicking)
button_stop.pack()

# List to store the click points
points = []

# Flag to control the clicking loop
running = False

# Start the main event loop
window.mainloop()
