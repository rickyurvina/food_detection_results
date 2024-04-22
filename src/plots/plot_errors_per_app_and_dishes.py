import matplotlib.pyplot as plt

from src.save_results import create_folder


def plot_bar_errors(data):
    # Obtener los nutrientes únicos
    nutrients = data['nutrient'].unique()
    plt.rc('font', size=12)

    # Iterar sobre los nutrientes
    save_dir = create_folder('bar_errors_per_app_and_dishes')
    for nutrient in nutrients:
        # Filtrar los datos para obtener solo las filas que corresponden a este nutriente
        nutrient_data = data[data['nutrient'] == nutrient]

        # Crear un gráfico de barras de los errores para cada plato, agrupados por app_name
        nutrient_data.groupby(['dish_id', 'app_name'])['error'].mean().unstack().plot(kind='bar', stacked=True)

        # Configurar el título y las etiquetas de los ejes
        plt.title(f'Error for {nutrient}')
        plt.xlabel('Dish ID')
        plt.ylabel(f'Error ({nutrient.capitalize()} - {get_unit(nutrient)})', fontsize=14)

        # Mostrar la leyenda y el gráfico
        plt.legend()
        plt.savefig(f'{save_dir}/bar_error_{nutrient}.png')
        plt.savefig(f'{save_dir}/bar_error_{nutrient}.svg')
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
