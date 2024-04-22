import matplotlib.pyplot as plt
from save_results import create_folder


def plots_statistics_box_plots(error_statistics):
    df = error_statistics.drop(columns=['app_id'])
    # Crear un gráfico de caja de bigotes para cada nutriente
    plt.rc('font', size=12)

    save_dir = create_folder('error_statistics')
    for nutrient in df['nutrient'].unique():
        fig, ax = plt.subplots(figsize=(12, 8))
        nutrient_data = df[df['nutrient'] == nutrient]
        app_names = nutrient_data['app_name'].unique()
        positions = range(1, len(app_names) + 1)
        max_error = 0
        min_error = 0
        for i, app_name in zip(positions, app_names):
            app_data = nutrient_data[nutrient_data['app_name'] == app_name]
            error_values = [app_data['min_error'].values[0],
                            app_data['mean_error'].values[0] - app_data['std_error'].values[0],
                            app_data['mean_error'].values[0],
                            app_data['mean_error'].values[0] + app_data['std_error'].values[0],
                            app_data['max_error'].values[0]]
            plt.boxplot(error_values, positions=[i], vert=True)
            max_error = max(max_error, max(error_values))
            min_error = min(min_error, min(error_values))
        ax.set_xticks([])
        plt.title(f'Error for {nutrient}', fontsize=16)
        plt.xlabel('App Name', fontsize=14)
        plt.ylabel(f'{nutrient.capitalize()} - {get_unit(nutrient)}', fontsize=14)
        # Ajustar el límite del eje y para dejar espacio para los nombres de las aplicaciones en la parte superior
        plt.ylim(0, max_error + 0.1 * (max_error - min_error))
        for i, app_name in zip(positions, app_names):
            plt.text(i, max_error + 0.03 * (max_error - min_error), app_name, ha='center', va='bottom',
                     fontsize=12)
        plt.savefig(f'{save_dir}/boxplot_error_{nutrient}.png')
        plt.savefig(f'{save_dir}/boxplot_error_{nutrient}.svg')
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
