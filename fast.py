import time
import pyautogui

def auto_type(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            time.sleep(5) 
            pyautogui.typewrite(content)
    except FileNotFoundError:
        print("File not found. Please make sure 'text.txt' exists.")

if __name__ == "__main__":
    file_path = 'text.txt'
    auto_type(file_path)
