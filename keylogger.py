from pynput import keyboard

if __name__ == "main":
    listener = keyboard.Listener(on_press=keyPress)
