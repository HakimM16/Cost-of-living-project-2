from openai import OpenAI
from dotenv import load_dotenv
import os
import json

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

if __name__ == "__main__":
    load_dotenv()
    city_name = "Munich"  # Example city
    save_info_to_json(city_name)
    print(f"City info for {city_name} saved to city_averages.json")
