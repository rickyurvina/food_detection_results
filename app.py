from flask import Flask, Response
import json
from src.sum_nutrients_per_app_and_dishes import generate_reports

app = Flask(__name__)


@app.route('/')
def index():
    return '¡Hola, mundo! Este es mi primer API con Flask.'


def get_data():
    return generate_reports(plots=False)


@app.route('/mean', methods=['GET'])
def get_mean():
    try:
        results_data, _, _ = get_data()
        # Convertir el DataFrame a JSON
        results_json = results_data.to_json(orient='records')
        # Convertir la cadena de texto JSON en un objeto JSON
        results_obj = json.loads(results_json)
        return Response(json.dumps(results_obj, indent=2), mimetype='application/json')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {'error': 'An error occurred while processing the request.'}


@app.route('/error-results', methods=['GET'])
def get_error():
    try:
        _, results_data_with_error, _ = get_data()

        # Convertir el DataFrame a JSON
        results_json = results_data_with_error.to_json(orient='records')
        # Convertir la cadena de texto JSON en un objeto JSON
        results_obj = json.loads(results_json)
        return Response(json.dumps(results_obj, indent=2), mimetype='application/json')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {'error': 'An error occurred while processing the request.'}


#
@app.route('/statistics', methods=['GET'])
def get_statistics():
    try:
        _, _, mean_error = get_data()

        # Convertir el DataFrame a JSON
        results_json = mean_error.to_json(orient='records')
        # Convertir la cadena de texto JSON en un objeto JSON
        results_obj = json.loads(results_json)
        return Response(json.dumps(results_obj, indent=2), mimetype='application/json')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {'error': 'An error occurred while processing the request.'}


if __name__ == '__main__':
    app.run(debug=True)
