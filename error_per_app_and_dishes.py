import pandas as pd

def calculate_error(results_data):
    # Eliminar filas con valores faltantes
    # results_data = results_data.dropna()

    # Filtrar los datos para obtener solo las aplicaciones con id 2, 3, 4 y 1 (nutricionista)
    filtered_data = results_data[(results_data['app_id'].isin([1, 2, 3, 4, 5]))]

    # Calcular el error para cada ítem nutricional
    error_data = pd.DataFrame()

    for nutrient in ['calories', 'sugars', 'protein', 'carbohydrates', 'fats', 'sodium']:
        # Obtener los valores de la nutricionista
        nutricionist_values = filtered_data[filtered_data['app_id'] == 1][f'sum_{nutrient}']

        # Calcular el error para cada aplicación con respecto a la nutricionista
        for app_id in [2, 3, 4, 5]:
            app_name = filtered_data[filtered_data['app_id'] == app_id]['app_name'].values[0]
            error = abs(filtered_data[(filtered_data['app_id'] == app_id)][f'sum_{nutrient}'].values - nutricionist_values.values) / nutricionist_values.values * 100
            dish_ids = filtered_data[(filtered_data['app_id'] == app_id)]['dish_id'].values
            error_data = pd.concat([error_data, pd.DataFrame({
                'app_id': [app_id] * len(dish_ids),
                'app_name': [app_name] * len(dish_ids),
                'dish_id': dish_ids,
                'nutrient': [nutrient] * len(dish_ids),
                'error': error
            })])

    return error_data
