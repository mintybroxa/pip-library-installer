# precisa da biblioteca pyfiglet e tqdm

import pyfiglet
import os
import subprocess
from tqdm import tqdm
import time

ascii_banner = pyfiglet.figlet_format("pip library installer")
print(ascii_banner)
def install_library(library_name):
    """
    Faz o download de uma biblioteca usando pip e exibe o progresso.
    """
    print(f"Iniciando o download da biblioteca: {library_name}")
    
    # Simulação de progresso (não diretamente do pip, mas visualmente útil)
    with tqdm(total=100, desc="Progresso do download", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}%", colour="green") as progress_bar:
        process = subprocess.Popen(
            [f"pip install {library_name}"], 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        
        # Simula progresso enquanto aguarda o pip terminar
        for _ in range(10):
            time.sleep(0.5)
            progress_bar.update(10)
        
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(f"\nBiblioteca '{library_name}' instalada com sucesso!")
        else:
            print(f"\nErro ao instalar a biblioteca '{library_name}'. Detalhes:")
            print(stderr.decode("utf-8"))

# Input do usuário
library_name = input("Library name: ")
install_library(library_name)
