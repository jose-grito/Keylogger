from pynput import keyboard
from datetime import datetime

def on_press(key):
    with open(r"C:\Users\Equipo\Desktop\ejercicios_bat\registro.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {key}\n")
    print(f"Tecla: {key}")

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
