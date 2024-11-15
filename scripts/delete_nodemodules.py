import os
import shutil
from tqdm import tqdm

def delete_node_modules(root_path, folder_to_del="node_modules", ignore_dirs=None):
    """
    Exclui todas as pastas chamadas "node_modules" em uma estrutura de diretórios, incluindo subpastas.
    Ignora pastas especificadas na lista ignore_dirs.

    :param root_path: Caminho raiz para começar a busca.
    :param ignore_dirs: Lista de nomes de pastas a serem ignoradas (opcional).
    """
    if ignore_dirs is None:
        ignore_dirs = []

    # Coletar todas as pastas "node_modules" antes de iniciar a exclusão
    node_modules_paths = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        if folder_to_del in dirnames:
            node_modules_paths.append(os.path.join(dirpath, folder_to_del))

    # Excluir as pastas "folder_to_del" com progresso
    for path in tqdm(node_modules_paths, desc="Deleting folder", unit=" folder(s)"):
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"Erro ao excluir {path}: {e}")

# Exemplo de uso
if __name__ == "__main__":
    root = r"C:\Users\knucl\GitHub"
    ignore = ["front-end-mentor", "quick-test"]

    delete_node_modules(root, "node_modules", ignore_dirs=ignore)