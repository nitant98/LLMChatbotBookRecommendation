from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('openai_api_key')

# Function to get book recommendations from OpenAI GPT-4
def get_recommendation_from_openai(query):
    # Define the messages for the chat model
    messages = [
        {"role": "system", "content": "You are a helpful assistant that recommends books."},
        {"role": "user", "content": f"Recommend five books based on the following query: {query}. Provide the response in the format Book_name: Publisher: Year: Author: Genre: Description."}
    ]
    
    # Create a chat completion request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",  
        messages=messages,
        max_tokens=1000 
    )
    
    # Return the text of the assistant's message
    return response.choices[0].message['content'].strip()

# Route to handle user queries
@app.route('/query', methods=['POST'])
def query():
    # Get the data from the POST request
    data = request.json
    
    # Extract the query from the data
    query = data.get('query', '')
    
    # Get the recommendation from OpenAI
    response = get_recommendation_from_openai(query)
    
    # Return the recommendation as a JSON response
    return jsonify({"recommendations": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)