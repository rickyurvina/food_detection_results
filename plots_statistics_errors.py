import matplotlib.pyplot as plt
import pandas as pd


def plots_statistics(error_statistics):
    # Crear un DataFrame con los datos de ejemplo
    # data = {
    #     'app_name': ['Calorie-Mama', 'Snap-Calorie', 'FoodVisor', 'Calorie-Mama', 'Snap-Calorie', 'FoodVisor', 'Calorie-Mama', 'Snap-Calorie', 'FoodVisor', 'Calorie-Mama', 'Snap-Calorie', 'FoodVisor', 'Calorie-Mama', 'Snap-Calorie', 'FoodVisor', 'Calorie-Mama', 'Snap-Calorie', 'FoodVisor'],
    #     'nutrient': ['calories', 'calories', 'calories', 'carbohydrates', 'carbohydrates', 'carbohydrates', 'fats', 'fats', 'fats', 'protein', 'protein', 'protein', 'sodium', 'sodium', 'sodium', 'sugars', 'sugars', 'sugars'],
    #     'mean_error': [24.18756465, 39.75566414, 31.87335294, 37.54883316, 38.08903603, 38.79197254, 43.14296354, 63.89862858, 51.12990642, 33.46093236, 30.33038288, 38.2987372, 66.64812838, 66.84057714, 54.4172236, 132.1851344, 41.13861844, 127.145934],
    #     'std_error': [20.02987339, 39.66159119, 20.58745849, 24.91642791, 40.06250813, 30.43813679, 29.26541002, 77.65452036, 37.7517146, 25.1460974, 24.81943995, 28.63051109, 64.53439819, 58.56686702, 31.56185936, 213.7562246, 38.74410666, 213.0285859],
    #     'min_error': [0.580650861, 5.353359641, 0.763063172, 5.204653541, 1.656314806, 0.144025508, 1.199399142, 3.76468749, 5.941368971, 1.907358987, 0.296565904, 4.632154571, 2.148065429, 2.870002953, 5.682976789, 15.9859969, 4.48365025, 9.243700981],
    #     'max_error': [65.59161256, 152.9833779, 75.13799106, 92.43239063, 175.504305, 112.3142266, 99.36204965, 334.609253, 179.1068695, 83.05324048, 81.49441318, 107.8085645, 270.3042364, 219.1829824, 141.5985336, 1000.671148, 163.0966237, 1040.93959]
    # }
    df = error_statistics.drop(columns=['app_id'])

    # Crear un gráfico de caja de bigotes para cada nutriente
    for nutrient in df['nutrient'].unique():
        plt.figure(figsize=(10, 6))
        nutrient_data = df[df['nutrient'] == nutrient]
        for i, app_name in enumerate(nutrient_data['app_name'].unique(), start=1):
            app_data = nutrient_data[nutrient_data['app_name'] == app_name]
            error_values = [app_data['min_error'].values[0], app_data['mean_error'].values[0] - app_data['std_error'].values[0], app_data['mean_error'].values[0], app_data['mean_error'].values[0] + app_data['std_error'].values[0], app_data['max_error'].values[0]]
            plt.boxplot(error_values, positions=[i], vert=True)
        plt.title(f'Boxplot of Error for {nutrient}')
        plt.xlabel('App')
        plt.ylabel('Error')
        plt.xticks(range(1, len(nutrient_data['app_name'].unique()) + 1), nutrient_data['app_name'].unique())
        plt.show()