import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui as pg
import time
import random

def type_with_delay(text, delay):
    for char in text:
        pg.write(char)
        # Introduce a delay between key presses based on the speed setting
        time.sleep(delay)

def start_typing():
    content = text_entry.get("1.0", tk.END).strip()  # Get the content and remove leading/trailing whitespace
    if not content:
        messagebox.showwarning("Warning", "There is nothing to print.")
        return
    speed = speed_scale.get() / 1000  # Convert speed from milliseconds to seconds
    # Add a delay before typing starts
    time.sleep(7)
    # Type the content with the specified speed
    type_with_delay(content, speed)
    # Press enter after typing is complete
    pg.press("enter")

def humanized_speed():
    content = text_entry.get("1.0", tk.END).strip()  # Get the content and remove leading/trailing whitespace
    if not content:
        messagebox.showwarning("Warning", "There is nothing to print.")
        return
    # Generate a random speed between 10ms and 100ms
    random_speed = random.uniform(0.01, 0.1)
    # Set the scale value to the random speed
    speed_scale.set(random_speed * 1000)

def toggle_speed_panel():
    if speed_frame.winfo_ismapped():
        speed_frame.pack_forget()  # Hide the speed control panel
    else:
        speed_frame.pack(side=tk.BOTTOM, fill=tk.X)  # Show the speed control panel at the bottom

# GUI setup
root = tk.Tk()
root.title("PasterPro by sudhanshusr007")

# Define style for buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)  # Pack the button frame at the bottom

# Label for text entry
text_entry_label = tk.Label(root, text="Paste your text here:", font=("Helvetica", 12))
text_entry_label.pack()

# Text entry box (fill and expand to fit window size)
text_entry = tk.Text(root, height=15, width=60, font=("Helvetica", 12, "bold"))
text_entry.pack(fill=tk.BOTH, expand=True)

# Custom Speed button
custom_speed_button = ttk.Button(button_frame, text="Custom Speed", command=toggle_speed_panel, style="TButton")
custom_speed_button.pack(side=tk.LEFT, padx=5)

# Humanized Speed button
humanized_button = ttk.Button(button_frame, text="Humanized Speed", command=humanized_speed, style="TButton")
humanized_button.pack(side=tk.LEFT, padx=5)

# Start Typing button
start_button = ttk.Button(button_frame, text="Start Typing", command=start_typing, style="TButton")
start_button.pack(side=tk.LEFT, padx=5)

# Frame for the speed control panel
speed_frame = tk.Frame(root)

# Speed scale label
speed_label = tk.Label(speed_frame, text="Speed:", font=("Helvetica", 12))
speed_label.pack()

# Speed scale
speed_scale = tk.Scale(speed_frame, from_=1, to=100, orient=tk.HORIZONTAL, length=200, label="Delay (ms)", font=("Helvetica", 10))
speed_scale.set(50)  # Initial speed setting
speed_scale.pack()

root.mainloop()
