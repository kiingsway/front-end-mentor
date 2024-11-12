import tkinter as tk
from tkinter import filedialog
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
    
    # Definir o ícone do aplicativo para aparecer na barra de tarefas
    root.iconbitmap('scripts/app_icon.ico')  # Substitua 'app_icon.ico' pelo caminho do seu ícone

    # Carregar a imagem
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

    # Menu de contexto com opções de Fechar e Minimizar
    def show_context_menu(event):
        context_menu.tk_popup(event.x_root, event.y_root)

    # Fechar e minimizar a janela
    def close_window():
        root.destroy()

    def minimize_window():
        # Desativa o overrideredirect antes de minimizar
        root.overrideredirect(False)
        root.iconify()

    # Restaurar o overrideredirect quando restaurar a janela
    def on_deiconify(event):
        root.overrideredirect(True)

    # Criação do menu de contexto
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Minimizar", command=minimize_window)
    context_menu.add_command(label="Fechar", command=close_window)

    # Associar o menu de contexto ao botão direito do mouse
    root.bind("<Button-3>", show_context_menu)
    root.bind("<Map>", on_deiconify)  # Vincula a função de restauração

    # Ajustes finais
    root.wait_visibility(root)
    root.wm_attributes('-alpha', opacity)
    root.mainloop()


# root = tk.Tk()
# root.withdraw()  # Oculta a janela principal
# file_path = filedialog.askopenfilename()

# Caminho da imagem e nível de opacidade
create_overlay("./product-preview-card-component/design/desktop-design.jpg", opacity=0.5)