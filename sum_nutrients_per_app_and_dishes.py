from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from error_per_app_and_dishes import calculate_error
from error_statistics import calculate_error_statistics
from plots_statistics_errors import plots_statistics

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

    # Leer los datos de la base de datos en un DataFrame de Pandas
    results_data = pd.read_sql(sql_query, engine)

    # Guardar la tabla en un archivo Excel
    results_data.to_excel('sum_nutrients_per_app_and_dish.xlsx', index=False)

    # Calcular el error
    results_data_with_error = calculate_error(results_data)
    results_data_with_error.to_excel('nutrient_errors.xlsx', index=False)
    mean_error = calculate_error_statistics(results_data_with_error)
    plots_statistics(mean_error)
    mean_error.to_excel("error_statistics.xlsx", index=False)


except Exception as e:
    print(f"An error occurred: {str(e)}")
