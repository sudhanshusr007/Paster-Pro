import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui as pg
import time
import random

def type_with_delay(text, delay):
    for char in text:
        pg.write(char)
        root.update()
        time.sleep(delay)

def start_typing():
    try:
        with open("text.txt", "r") as file:
            content = file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'text.txt' not found.")
        return

    if not content:
        messagebox.showwarning("Warning", "There is nothing to print.")
        return

    speed = speed_scale.get()  # Speed is in words per minute

    if speed <= 0:
        messagebox.showwarning("Warning", "Speed should be greater than 0.")
        return

    # Convert speed from words per minute to characters per second
    chars_per_second = speed / 60 * 5  # Assuming an average word length of 5 characters

    # Calculate delay between characters in seconds
    delay = 1 / chars_per_second

    print("Starting typing...")
    type_with_delay(content, delay)
    print("Typing complete.")
    pg.press("enter")

def humanized_speed():
    # Not applicable for achieving a specific typing speed in this context
    pass

def toggle_speed_panel():
    if speed_frame.winfo_ismapped():
        speed_frame.pack_forget()
    else:
        speed_frame.pack(side=tk.BOTTOM, fill=tk.X)

root = tk.Tk()
root.title("PasterPro by sudhanshusr007")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

custom_speed_button = ttk.Button(button_frame, text="Custom Speed", command=toggle_speed_panel, style="TButton")
custom_speed_button.pack(side=tk.LEFT, padx=5)

humanized_button = ttk.Button(button_frame, text="Humanized Speed", command=humanized_speed, style="TButton")
humanized_button.pack(side=tk.LEFT, padx=5)

start_button = ttk.Button(button_frame, text="Start Typing", command=start_typing, style="TButton")
start_button.pack(side=tk.LEFT, padx=5)

speed_frame = tk.Frame(root)

speed_label = tk.Label(speed_frame, text="Speed (wpm):", font=("Helvetica", 12))
speed_label.pack()

speed_scale = tk.Scale(speed_frame, from_=0, to=2000, orient=tk.HORIZONTAL, length=200, label="Speed (wpm)", font=("Helvetica", 10))
speed_scale.set(1000)  # Default speed set to 1000 wpm
speed_scale.pack()

root.mainloop()
