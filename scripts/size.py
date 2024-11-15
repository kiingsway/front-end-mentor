import os
from prettytable import PrettyTable

def format_size(size_in_bytes):
    """
    Formata o tamanho de bytes para KB, MB ou GB com duas casas decimais.
    """
    if size_in_bytes < 1024:
        return f"{size_in_bytes} Bytes"
    elif size_in_bytes < 1024**2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024**3:
        return f"{size_in_bytes / 1024**2:.2f} MB"
    else:
        return f"{size_in_bytes / 1024**3:.2f} GB"

def get_folder_sizes(path):
    """
    Calcula o tamanho de cada pasta no primeiro nível do diretório especificado.
    Retorna uma lista de tuplas contendo o nome da pasta e seu tamanho em bytes.
    """
    folder_sizes = []
    try:
        for folder_name in os.listdir(path):
            folder_path = os.path.join(path, folder_name)
            if os.path.isdir(folder_path):
                total_size = 0
                for dirpath, _, filenames in os.walk(folder_path):
                    total_size += sum(
                        os.path.getsize(os.path.join(dirpath, file)) for file in filenames
                    )
                folder_sizes.append((folder_name, total_size))
    except Exception as e:
        print(f"Erro ao acessar o diretório: {e}")
    return folder_sizes

def display_report(folder_sizes):
    """
    Exibe um relatório visual das pastas e seus tamanhos em formato de tabela, classificado pelo mais pesado.
    """
    # Classificar pelo tamanho (descendente)
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    table = PrettyTable()
    table.field_names = ["Folder Name", "Size"]
    for folder_name, size in folder_sizes:
        table.add_row([folder_name, format_size(size)])
    print(table)

# Caminho fornecido pelo usuário
folder_path = r"C:\Users\knucl\GitHub"

# Obtém os tamanhos das pastas e exibe o relatório
folder_sizes = get_folder_sizes(folder_path)
display_report(folder_sizes)
