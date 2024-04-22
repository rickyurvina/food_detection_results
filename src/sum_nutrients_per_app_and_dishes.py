from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from src.error_per_app_and_dishes import calculate_error
from src.error_statistics import calculate_error_statistics
from src.plot_errors_per_app_and_dishes import plot_bar_errors
from src.plots_bar_mean_errors import plot_mean_errors
from src.plots_statistics_errors import plots_statistics_box_plots
from src.save_results import create_folder


def generate_reports():
    try:
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()

        # Leer las credenciales de la base de datos desde las variables de entorno
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')
        host = os.getenv('MYSQL_HOST')
        database = os.getenv('MYSQL_DATABASE')

        # Establecer la conexión a la base de datos usando SQLAlchemy
        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

        # Consulta SQL para obtener el total de calorías por plato
        sql_query = """
            SELECT r.app_id, a.name AS app_name, m.dish_id, d.name AS dish_name,
                   SUM(r.calories) AS sum_calories,
                   SUM(r.sugars) AS sum_sugars,
                   SUM(r.protein) AS sum_protein,
                   SUM(r.carbohydrates) AS sum_carbohydrates,
                   # SUM(r.fiber) AS sum_fiber,
                   SUM(r.fats) AS sum_fats,
                   SUM(r.sodium) AS sum_sodium
            FROM results_meals AS r
            LEFT JOIN meals AS m ON r.meal_id = m.meal_id
            LEFT JOIN apps AS a ON r.app_id = a.app_id
            LEFT JOIN dishes AS d ON m.dish_id = d.dish_id
            GROUP BY r.app_id, m.dish_id
        """

        results_data = pd.read_sql(sql_query, engine)
        results_data_with_error = calculate_error(results_data)
        mean_error = calculate_error_statistics(results_data_with_error)
        plots_charts(results_data, results_data_with_error, mean_error)
        # save_files(results_data, results_data_with_error, mean_error)


    except Exception as e:
        print(f"An error occurred: {str(e)}")

def save_files(results_data, results_data_with_error, mean_error):
    save_dir = create_folder('data_results', is_file=True)
    results_data.to_excel(f'{save_dir}/sum_nutrients_per_app_and_dish.xlsx', index=False)
    results_data_with_error.to_excel(f'{save_dir}/nutrient_errors.xlsx', index=False)
    mean_error.to_excel(f'{save_dir}/error_statistics.xlsx', index=False)
def plots_charts(results_data, results_data_with_error, mean_error):
    plots_statistics_box_plots(mean_error)
    plot_bar_errors(results_data_with_error)
    plot_mean_errors(mean_error)

