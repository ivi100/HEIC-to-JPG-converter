#Ivan Manuel Gambero Galvez
#Convertidor de archivo HEIC a JPG

import os
import subprocess

def convert_heic_to_jpg_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".heic", ".jpg"))

            try:
                # Usar heif-convert con las opciones adecuadas
                subprocess.run(['heif-convert', input_path, '-o', output_path, '-f', 'jpg'], check=True)
                print(f"Convertido: {input_path} a {output_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error al convertir {input_path}: {e}")

print("Programa realizado por Ivan Manuel Gambero Galvez\n")

input_folder_path = input("Introduzca direccion de la carpeta de entrada: ")
output_folder_path = input("Introduzca direccion de la carpeta de salida: ")

convert_heic_to_jpg_folder(input_folder_path, output_folder_path)

print("\nCONVERSION LISTA.")

input("Pulsa ENTER para finalizar")
