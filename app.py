from flask import Flask, render_template, request, jsonify
import json
import os

API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

# Load JSON Data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'city_averages.json')

# Load the average costs when the app starts
with open(DATA_PATH, 'r') as f:
    AVERAGE_COSTS = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    try:
        # Input data from user
        data = request.json
        city1 = data['city1']
        city2 = data['city2']
        expenses_city1 = data['expenses_city1']
        total_income = data.get('total_income', None)
        
        # Average costs for city 2
        city2_avg = AVERAGE_COSTS.get(city2, {})

        # Calculate total expenses
        total_city1 = sum(expenses_city1.values())
        total_city2 = sum(city2_avg.values())

        return jsonify({
            "city1": city1,
            "city2": city2,
            "expenses_city1": expenses_city1,
            "average_city2": city2_avg,
            "totals": {"city1": total_city1, "city2": total_city2},
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/data', methods=['GET'])
def get_api_data():
    if not API_KEY:
        return jsonify({"error": "API key is missing"}), 500
    return jsonify({"apiKey": API_KEY})  # Return JSON with the API key

if __name__ == "__main__":
    app.run(debug=True)
