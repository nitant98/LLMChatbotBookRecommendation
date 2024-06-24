import streamlit as st
import requests

# Set the title of the Streamlit app
st.title("Book Recommendation Chatbot")

# Display instructions for the user
st.markdown("""
## Instructions
Please start your query with the word **"book"**. For example:
- "book like 'To Kill a Mockingbird'"
- "book with genre science fiction"
- "book published in 2020"
""")

# Input field for the user to enter their query
query = st.text_input("Ask me for book recommendations or information!")

# Button to submit the query
if st.button("Submit"):
    if query.lower().startswith("book"):
        # Send the query to the backend Flask server
        response = requests.post("http://127.0.0.1:5000/query", json={"query": query})
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Get the recommendations from the JSON response
            recommendations = response.json().get("recommendations", "Sorry, I couldn't process your request.")
            
            # Display the recommendations in a formatted way
            st.markdown("## Book Recommendations")
            for rec in recommendations.split("\n\n"):
                if rec.strip(): 
                    # Split the recommendation into its components
                    parts = rec.split(": ")
                    if len(parts) == 6:  # Including description
                        book_name, publisher, year, author, genre, description = parts
                        st.markdown(f"**Book Name:** {book_name}\n**Publisher:** {publisher}\n**Year:** {year}\n**Author:** {author}\n**Genre:** {genre}\n**Description:** {description}")
                        st.markdown("---")
        else:
            # Display an error message if something went wrong
            st.write("Sorry, something went wrong with the request.")
    else:
        # Display a message asking the user to start the query with "book"
        st.write("Please start your query with the word 'book'.")
