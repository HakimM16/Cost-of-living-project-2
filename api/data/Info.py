import openai
import os
from dotenv import load_dotenv

async def generate_response(city1, city2):
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
    client = openai.OpenAI(
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
    client = openai.OpenAI(
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

# Example usage
if __name__ == "__main__":
    # For async version (requires asyncio.run())
    import asyncio
    
    # Async example
    result = asyncio.run(generate_response("Los Angeles", "New York"))
    
    # Sync example
    # result = generate_response_sync("Los Angeles", "New York")