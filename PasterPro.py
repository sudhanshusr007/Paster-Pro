import pyautogui as pg
import time
import random

def type_with_delay(text):
    for char in text:
        pg.write(char)
        # Introduce a shorter random delay between key presses
        time.sleep(random.uniform(0.001, 0.05))  # Adjust the range as needed

def main():
    with open('text.txt', 'r') as f:
        content = f.read()
        content = content.replace("  ", "")

    # Add a delay before typing starts
    time.sleep(7)

    # Type the content with shorter random delays between key presses
    type_with_delay(content)

    # Press enter after typing is complete
    pg.press("enter")

if __name__ == "__main__":
    main()
