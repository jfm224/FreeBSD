import os
import subprocess
from pyinsane2 import pyinsane

def scan_image():
    # Inicializa o SANE
    pyinsane.init()

    # Lista os dispositivos disponíveis
    devices = pyinsane.get_devices()
    if not devices:
        print("Nenhum scanner encontrado.")
        return

    # Seleciona o primeiro scanner disponível
    scanner = devices[0]
    print(f"Usando o scanner: {scanner}")

    # Inicia o processo de escaneamento
    print("Escaneando...")
    scan_session = pyinsane.Scanner(scanner)
    image = scan_session.scan()

    # Salva a imagem escaneada
    output_file = "scanned_image.png"
    image.save(output_file)
    print(f"Imagem salva como {output_file}")

    # Abre a imagem escaneada no Eye of GNOME
    subprocess.run(['eog', output_file])

if __name__ == "__main__":
    scan_image()

