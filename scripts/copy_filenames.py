import os

def copiar_nomes_arquivos(pasta):
    arquivos = [f'"{arquivo}"' for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))]
    nomes_formatados = ', '.join(arquivos)
    return nomes_formatados

# Caminho da pasta que contém os arquivos
pasta = f'order-summary-component/assets/fonts/Red_Hat_Display/static'
resultado = copiar_nomes_arquivos(pasta)
print(resultado)
