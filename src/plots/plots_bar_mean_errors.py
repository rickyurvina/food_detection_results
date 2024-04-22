import matplotlib.pyplot as plt
import pandas as pd

from src.save_results import create_folder


def plot_mean_errors(data):
    # Configurar el tamaño y el peso de la fuente global
    # plt.rc('font', size=12, weight='bold')
    plt.rc('font', size=12)

    # Obtener los nutrientes únicos
    nutrients = data['nutrient'].unique()
    save_dir = create_folder('mean_errors')

    # Iterar sobre los nutrientes
    for nutrient in nutrients:
        # Filtrar los datos para obtener solo las filas que corresponden a este nutriente
        nutrient_data = data[data['nutrient'] == nutrient]
        app_names = nutrient_data['app_name'].unique()


        # Crear un gráfico de barras de los errores medios para cada aplicación
        bar_plot = nutrient_data.groupby('app_name')['mean_error'].mean().plot(kind='bar', color='lightgray')

        # Configurar el título y las etiquetas de los ejes
        plt.title(f'Mean Error for {nutrient}')
        # plt.xlabel('App Name')
        plt.ylabel(f'{nutrient.capitalize()} - {get_unit(nutrient)}')

        # Calcular el valor máximo de mean_error
        max_error = nutrient_data['mean_error'].max()

        # Establecer el rango del eje y
        plt.xlabel('App Name')
        plt.ylim(0, max(100, max_error + 10))
        bar_plot.set_xticklabels(app_names, rotation=45, ha='right')

        # Agregar texto en la parte superior de cada barra
        for i, v in enumerate(nutrient_data.groupby('app_name')['mean_error'].mean()):
            plt.text(i, v + 1, f'{v:.2f}', ha='center')

        plt.tight_layout()
        plt.savefig(f'{save_dir}/mean_error_{nutrient}.png')
        plt.savefig(f'{save_dir}/mean_error_{nutrient}.svg')
        plt.show()


def get_unit(nutrient):
    # Definir las unidades para cada nutriente
    units = {
        'calories': 'kcal',
        'sugars': 'g',
        'protein': 'g',
        'carbohydrates': 'g',
        'fiber': 'g',
        'fats': 'g',
        'sodium': 'mg'
    }
    return units.get(nutrient, '')
