# Book Recommendation Chatbot

This project is a simple book recommendation chatbot using Streamlit for the frontend and Flask with OpenAI GPT-4 for the backend.

## Domain Selection

**Domain:** Book Recommendations

**User Base:**
- Avid readers looking for new books to read.
- Students seeking books related to their studies.
- Casual readers looking for popular or trending books.
- Readers interested in specific genres, authors, or book series.

**Application Scope:**
- Recommend books based on genre, author, or title.
- Provide book details like summary, author, publication year, and user reviews.
- Suggest books based on user's reading history or preferences.
- Answer queries about book series order, new releases, and popular books in specific categories.

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Flask
- OpenAI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/book-recommendation-chatbot.git
   cd book-recommendation-chatbot
    ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your_openai_api_key'
   ```

### Installation

1. Start the Flask backend:
   ```
   python backend.py
   ```
2. Start the Streamlit frontend:
   ```
   streamlit run app.py
   ```
3. Open your browser and go to http://localhost:8501 to interact with the chatbot.

## Usage

To use the chatbot, type your book-related query into the input field on the application's interface and click "Submit". Ensure each query starts with the word "book". The chatbot will respond with book recommendations or information based on your query.

### Example Queries

- "book like 'To Kill a Mockingbird'"
- "book with genre science fiction"
- "book published in 2020"

### Example Output

Upon submitting a query, the chatbot will provide recommendations in the following format:

- **Book Name:** [Book Name]
- **Publisher:** [Publisher]
- **Year:** [Year]
- **Author:** [Author]
- **Genre:** [Genre]
- **Description:** [Description]

Recommendations will be separated by a line.

## File Structure

- `backend.py`: Contains the Flask backend, which processes user queries and interfaces with the OpenAI GPT-4 API.
- `app.py`: Implements the Streamlit frontend, which manages the user interface for entering queries and displaying recommendations.
- `.env`: OpenAI api key stored in environement to secure it.

## Video Demonstration


