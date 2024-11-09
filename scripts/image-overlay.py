import tkinter as tk
from PIL import Image, ImageTk
import json
import os

def load_position(image_name):
    """Carrega a posição salva da janela para uma imagem específica."""
    if os.path.exists("positions.json"):
        with open("positions.json", "r") as file:
            positions = json.load(file)
        return positions.get(image_name, "+100+100")  # Posição padrão se não houver registro
    return "+100+100"

def save_position(image_name, x, y):
    """Salva a posição atual da janela para uma imagem específica."""
    if os.path.exists("positions.json"):
        with open("positions.json", "r") as file:
            positions = json.load(file)
    else:
        positions = {}
    positions[image_name] = f"+{x}+{y}"
    with open("positions.json", "w") as file:
        json.dump(positions, file)

def create_overlay(image_path, opacity=0.5):
    root = tk.Tk()
    root.title("Image Overlay")

    def close(event): root.destroy()
    root.bind("<Button-3>", close)

    image = Image.open(image_path).convert("RGBA")
    tk_image = ImageTk.PhotoImage(image)

    root.overrideredirect(True)
    root.attributes("-topmost", True)

    label = tk.Label(root, image=tk_image, bg='white')
    label.pack()

    # Nome único para a imagem atual
    image_name = os.path.basename(image_path)
    
    # Restaurar posição salva
    root.geometry(load_position(image_name))

    # Função para movimentar a janela e salvar a posição
    def move_window(event):
        x, y = event.x_root, event.y_root
        root.geometry(f'+{x}+{y}')
        save_position(image_name, x, y)
    label.bind("<B1-Motion>", move_window)

    root.wait_visibility(root)
    root.wm_attributes('-alpha', opacity)
    root.mainloop()

# Caminho da imagem e nível de opacidade
create_overlay("./order-summary-component/design/desktop-design.jpg", opacity=0.5)
