from pynput.keyboard import Controller
from pynput import keyboard

contro = Controller()


pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)

    if keyboard.Key.cmd in pressed_keys and keyboard.Key.shift in pressed_keys:
        try:
            char = key.char
        except AttributeError:
            return
        if char == "8":
            contro.type("[")
        elif char == "9":
            contro.type("]")

    if keyboard.Key.cmd in pressed_keys and not keyboard.Key.shift in pressed_keys:
        try:
            char = key.char
        except AttributeError:
            return
        if char == "8":
            contro.type("{")
        elif char == "9":
            contro.type("}")

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)


with keyboard.Listener(
    on_press = on_press,
    on_release = on_release
) as listener:
    listener.join()
