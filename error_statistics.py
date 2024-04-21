import pandas as pd
import numpy as np

def calculate_error_statistics(error_report):
    # Eliminar filas con valores faltantes
    # error_report = error_report.dropna()

    # Obtener todos los valores únicos de app_id y nutrient
    unique_app_ids = error_report['app_id'].unique()
    unique_nutrients = error_report['nutrient'].unique()

    # Crear un DataFrame vacío para almacenar los resultados
    error_statistics = pd.DataFrame(columns=['app_id', 'app_name', 'nutrient', 'mean_error', 'std_error', 'min_error', 'max_error'])

    # Iterar sobre todos los valores únicos de app_id y nutrient
    for app_id in unique_app_ids:
        for nutrient in unique_nutrients:
            # Filtrar el DataFrame para el app_id y el nutriente específicos
            filtered_errors = error_report[(error_report['app_id'] == app_id) & (error_report['nutrient'] == nutrient)]

            # Calcular las estadísticas de errores
            mean_error = np.mean(filtered_errors['error'])
            std_error = np.std(filtered_errors['error'])
            min_error = np.min(filtered_errors['error'])
            max_error = np.max(filtered_errors['error'])

            # Obtener el nombre de la aplicación
            app_name = filtered_errors['app_name'].iloc[0]

            # Agregar el resultado al DataFrame de estadísticas de errores
            error_statistics = error_statistics.append({'app_id': app_id, 'app_name': app_name, 'nutrient': nutrient,
                                                         'mean_error': mean_error, 'std_error': std_error,
                                                         'min_error': min_error, 'max_error': max_error},
                                                        ignore_index=True)

    return error_statistics
