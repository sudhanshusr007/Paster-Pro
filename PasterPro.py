import pyautogui as pg
import time

def type_with_delay(text, delay):
    for char in text:
        pg.write(char)
        time.sleep(delay)

def main():
    with open('text.txt', 'r') as f:
        content = f.read()
        content = content.replace("  ", "")

    # Calculate the number of characters in the text
    num_characters = len(content)

    # Set target typing speed (characters per minute)
    target_speed = 80000000

    # Calculate time per character
    time_per_character = 0.1 / target_speed

    # Type the content with the calculated delay between key presses
    type_with_delay(content, time_per_character)

    # Press enter after typing is complete
    pg.press("enter")

if __name__ == "__main__":
    main()
