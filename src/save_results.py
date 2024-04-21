import os
import datetime

def create_folder(folder_name, is_file=False):
    # Obtener la fecha actual y formatearla como YYYYMMDD
    date_str = datetime.datetime.now().strftime('%Y%m%d')

    # Comprobar si el directorio 'results/images' o 'results/files' existe, si no, crearlo
    folder_type = 'files' if is_file else 'images'
    if not os.path.exists(f'results/{folder_type}'):
        os.makedirs(f'results/{folder_type}')

    # Crear el nombre de la nueva carpeta
    new_folder_name = f'{date_str}_{folder_name}_1'
    new_folder_path = os.path.join('results', folder_type, new_folder_name)

    # Comprobar si ya existe una carpeta con el mismo nombre
    counter = 1
    while os.path.exists(new_folder_path):
        counter += 1
        new_folder_name = f'{date_str}_{folder_name}_{counter}'
        new_folder_path = os.path.join('results', folder_type, new_folder_name)

    # Crear la nueva carpeta
    os.makedirs(new_folder_path)

    return new_folder_path