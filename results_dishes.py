import pandas as pd
from sqlalchemy import create_engine

# Establecer la conexión a la base de datos usando SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:12345678@localhost/fooddetection')

# Consulta SQL para obtener el total de calorías por plato
sql_query = """
    SELECT r.app_id, m.dish_id, SUM(r.calories) AS sum_calories
    FROM results_meals AS r
    INNER JOIN meals AS m ON r.meal_id = m.meal_id
    GROUP BY r.app_id, m.dish_id
"""


# Leer los datos de la base de datos en un DataFrame de Pandas
results_data = pd.read_sql(sql_query, engine)
results_data.to_excel('sum_calories_per_app_and_dish.xlsx', index=False)

print("Tabla guardada exitosamente en 'sum_calories_per_app_and_dish.xlsx'")
# Mostrar la tabla con el total de calorías por plato
print("Total Calories per Dish:")
print(results_data)