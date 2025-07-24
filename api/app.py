from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import json
import os
#from AI import save_info_to_json
#from Info import generate_response_sync

def generate_city_info(city_name):
    """Generates a structured JSON response with average cost of living in a given city using OpenAI's API."""

    client = OpenAI()

    client.api_key = os.getenv("OPENAI_API_KEY")

    system_prompt = {
        "role": "system",
        "content": "You are a helpful assistant that provides average cost of expenses in £ in a given city for a month. "
        "Expenses included must be rent, fitness, food, clothes, transport, debts, luxuries, utilities.  You must provide the information in a structured JSON format."
        "Example: {'Paris': {'rent': 11472,'fitness': 29,'food': 294,'clothes': 78,'transport': 57,'debts': 0,'luxuries': 41,'utilities': 235.00}}"
    }
    user_prompt = {
        "role": "user",
        "content": f"Provide a detailed overview of the cost of living in {city_name}."
    }

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            system_prompt,
            user_prompt
        ]
    )
    return response.choices[0].message.content

def save_info_to_json(city_name):
    """ Save the generated city info to a JSON file. """
    city_info_str = generate_city_info(city_name)
    city_info = json.loads(city_info_str)  # Convert string to dict
    with open("averages.json", "w") as json_file:
        json.dump(city_info, json_file, indent=2)
        json_file.close()

def generate_response(city1, city2):
    """
    Generate a cost of living comparison between two cities using OpenAI API
    
    Args:
        city1 (str): First city for comparison
        city2 (str): Second city for comparison
    
    Returns:
        str: HTML formatted response or None if error occurs
    """
    
    # Load environment variables from .env file
    load_dotenv(r'C:\Users\hakim\OneDrive\Desktop\Cost of living project 2\.env')
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    system_prompt = {
        'role': 'system',
        'content': """You are a helpful assistant that generates detailed written summaries explaining why costs differ between cities (e.g., "San Francisco housing costs are 60% higher due to tech industry demand and limited housing supply").
        You create personalized recommendations based on the user's expense patterns and lifestyle preferences.You also generate monthly and annual budget projections, providing context about seasonal variations.
        Ensure to handle errors gracefully and provide clear, informative responses to the user. You must produce the response in html format, with appropriate headings and paragraphs for clarity.
        This is an example response in comparing Los Angeles and New York City:
        <div class="container">
            <h1>Los Angeles vs New York Cost of Living Analysis</h1>
            <div class="section">
                <h2>Why Costs Differ</h2>
                <p><strong>Housing:</strong> <span class="highlight">New York requires approximately 38% more income to maintain the same standard of living as Los Angeles</span>, driven by Manhattan's extreme real estate scarcity versus LA's sprawling geography with more available land.</p>
                <div class="cost-stat">
                    <strong>Daily Expenses:</strong> NYC residents spend around $485/month on groceries compared to $375/month in Los Angeles due to higher commercial rents and import logistics costs in NYC.
                </div>
            </div>
            <div class="section">
                <h2>Personalised Recommendations</h2>
                <p><strong>Young Professionals:</strong> NYC's higher costs may be justified by networking opportunities, though <span class="highlight">NYC employers typically pay 4.6% more than LA employers</span> - not enough to fully offset the cost difference.</p>
                <p><strong>Families & Remote Workers:</strong> LA offers more space per dollar and becomes especially attractive without needing NYC salary premiums.</p>
            </div>
            <div class="section">
                <h2>Budget Projections</h2>
                <div class="cost-stat">
                    <strong>Annual Impact:</strong> To maintain a $17,000 lifestyle in NYC, you'd only need about $11,997 in Los Angeles - potential savings of $5,000+ annually.
                </div>
                <p><strong>Seasonal Variations:</strong> NYC sees 15-20% higher winter expenses (heating, clothing) while LA's consistent climate reduces utility fluctuations. <span class="highlight">LA residents have 1.5 months expense coverage versus 1.2 months in NYC</span>, providing better financial flexibility.</p>
            </div>
            <div class="bottom-line">
                <strong>Bottom Line:</strong> LA offers superior financial breathing room for most lifestyles, while NYC commands a premium for unique urban advantages.
            </div>
        </div>"""
    }
    
    user_prompt = {
        'role': 'user',
        'content': f'Please compare the cost of living between {city1} and {city2}.'
    }
    
    try:
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[system_prompt, user_prompt]
        )
        
        assistant_message = response.choices[0].message
        print(assistant_message.content)
        return assistant_message.content
        
    except Exception as error:
        print(f'Error generating response: {error}')
        return None

# Synchronous version (if you don't need async)
def generate_response_sync(city1, city2):
    """
    Synchronous version of generate_response function
    
    Args:
        city1 (str): First city for comparison
        city2 (str): Second city for comparison
    
    Returns:
        str: HTML formatted response or None if error occurs
    """
    
    # Load environment variables from .env file
    load_dotenv(r'C:\Users\hakim\OneDrive\Desktop\Cost of living project 2\.env')
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    system_prompt = {
        'role': 'system',
        'content': """You are a helpful assistant that generates detailed written summaries explaining why costs differ between cities (e.g., "San Francisco housing costs are 60% higher due to tech industry demand and limited housing supply").
        You create personalized recommendations based on the user's expense patterns and lifestyle preferences.You also generate monthly and annual budget projections, providing context about seasonal variations.
        Ensure to handle errors gracefully and provide clear, informative responses to the user. You must produce the response in html format, with appropriate headings and paragraphs for clarity.
        This is an example response in comparing Los Angeles and New York City:
        <div class="container">
            <h1>Los Angeles vs New York Cost of Living Analysis</h1>
            <div class="section">
                <h2>Why Costs Differ</h2>
                <p><strong>Housing:</strong> <span class="highlight">New York requires approximately 38% more income to maintain the same standard of living as Los Angeles</span>, driven by Manhattan's extreme real estate scarcity versus LA's sprawling geography with more available land.</p>
                <div class="cost-stat">
                    <strong>Daily Expenses:</strong> NYC residents spend around $485/month on groceries compared to $375/month in Los Angeles due to higher commercial rents and import logistics costs in NYC.
                </div>
            </div>
            <div class="section">
                <h2>Personalised Recommendations</h2>
                <p><strong>Young Professionals:</strong> NYC's higher costs may be justified by networking opportunities, though <span class="highlight">NYC employers typically pay 4.6% more than LA employers</span> - not enough to fully offset the cost difference.</p>
                <p><strong>Families & Remote Workers:</strong> LA offers more space per dollar and becomes especially attractive without needing NYC salary premiums.</p>
            </div>
            <div class="section">
                <h2>Budget Projections</h2>
                <div class="cost-stat">
                    <strong>Annual Impact:</strong> To maintain a $17,000 lifestyle in NYC, you'd only need about $11,997 in Los Angeles - potential savings of $5,000+ annually.
                </div>
                <p><strong>Seasonal Variations:</strong> NYC sees 15-20% higher winter expenses (heating, clothing) while LA's consistent climate reduces utility fluctuations. <span class="highlight">LA residents have 1.5 months expense coverage versus 1.2 months in NYC</span>, providing better financial flexibility.</p>
            </div>
            <div class="bottom-line">
                <strong>Bottom Line:</strong> LA offers superior financial breathing room for most lifestyles, while NYC commands a premium for unique urban advantages.
            </div>
        </div>"""
    }
    
    user_prompt = {
        'role': 'user',
        'content': f'Please compare the cost of living between {city1} and {city2}.'
    }
    
    try:
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[system_prompt, user_prompt]
        )
        
        assistant_message = response.choices[0].message
        #print(assistant_message.content)
        return assistant_message.content
        
    except Exception as error:
        print(f'Error generating response: {error}')
        return None

API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    try:
        # Input data from user
        data = request.json

        save_info_to_json(data['city2'])  # Save city2 info to JSON

        # Load the average costs from the JSON file
        DATA_PATH = os.path.join('averages.json')
        if not os.path.exists(DATA_PATH):
            return jsonify({"error": "Data file not found"}), 500

        # Load the average costs when the app starts
        with open(DATA_PATH, 'r') as f:
            AVERAGE_COSTS = json.load(f)

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

@app.route('/generate-response', methods=['POST'])
def generate_response():
    try:
        data = request.json
        city1 = data.get('city1')
        city2 = data.get('city2')
        # Call your OpenAI function (make sure it returns a string or dict)
        response = generate_response_sync(city1, city2)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)


