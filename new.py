import tkinter as tk
import pyautogui as pg
import time
import random

def type_with_delay(text):
    for char in text:
        pg.write(char)
        # Introduce a shorter random delay between key presses
        time.sleep(random.uniform(0.001, 0.05))  # Adjust the range as needed

def start_typing():
    content = text_entry.get("1.0", tk.END)
    content = content.replace("  ", "")
    # Add a delay before typing starts
    time.sleep(7)
    # Type the content with shorter random delays between key presses
    type_with_delay(content)
    # Press enter after typing is complete
    pg.press("enter")

# GUI setup
root = tk.Tk()
root.title("PasterPro by sudhanshusr007")

text_entry_label = tk.Label(root, text="Paste your text here:")
text_entry_label.pack()

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack(pady=20)

root.mainloop()
