import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
book_data = pd.read_csv('data/prepared_bookdata.csv')

# Rename columns
book_data.rename(columns={'authors': 'Authors', 'description': 'Description', 'publisher': 'Publisher', 'publishedDate':'Published Date', 'rating': 'Rating', 'categories':'Categories', 'ratingsCount': 'Ratings Count'}, inplace=True)

# Combine relevant text fields into a single text input 
book_data['combined_text'] = book_data.apply(lambda row: ' '.join([
    str(row['Title']),
    str(row['Description']),
    str(row['Authors']),
    str(row['Publisher']),
    str(row['Published Date']),
    str(row['Categories'])
]), axis=1)

# Create a mapping from book titles to their indices
indices = pd.Series(book_data.index, index=book_data['Title']).drop_duplicates()

# Create TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Transform documents into TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(book_data['combined_text'])

# Function to calculate cosine similarity
def calculate_similarity_on_demand(idx, tfidf_matrix):
    cosine_similarities = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    return cosine_similarities

# Define recommendation function to find similar books
def get_recommendations_on_demand(query, search_by= 'title', n_recommendations=10):
    sim_scores = None
    if search_by == 'title':
        # Filter books where title starts with the query
        filtered_indices = book_data[book_data['Title'].str.startswith(query, na=False)].index
        sim_scores = np.zeros(len(book_data))  # Initialize similarity scores array
        for idx in filtered_indices:
            sim_scores += calculate_similarity_on_demand(idx, tfidf_matrix)
        sim_scores /= len(filtered_indices)  # Average similarity scores across filtered books
    elif search_by == 'Authors':
        # Filter books where author contains the query
        filtered_indices = book_data[book_data['Authors'].str.contains(query, case=False, regex=False)].index
        sim_scores = np.zeros(len(book_data))  # Initialize similarity scores array
        for idx in filtered_indices:
            sim_scores += calculate_similarity_on_demand(idx, tfidf_matrix)
        sim_scores /= len(filtered_indices)  # Average similarity scores across filtered books
    
    if sim_scores is not None:
        sim_scores = list(enumerate(sim_scores))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        book_indices = [i[0] for i in sim_scores[:n_recommendations]]
        
        recommendations = book_data[['Title', 'Authors', 'Categories', 'Rating', 'Ratings Count', 'Published Date']].iloc[book_indices]
        recommendations['Similarity Score'] = [score for _, score in sim_scores[:n_recommendations]]
        
        return recommendations
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no valid search_by option

# Clean author names by removing the square brackets
book_data['Authors'] = book_data['Authors'].apply(lambda x: x.strip("[]").replace("'", ""))

# Clean category names (if needed)
book_data['Categories'] = book_data['Categories'].apply(lambda x: x.strip("[]").replace("'", ""))

# Streamlit interface
st.title('Book Recommender')

# User selection for search by title or author
search_by = st.radio('Search by:', ('Title', 'Authors'))

# Depending on user choice, display a dropdown to select either a Title or an Author
if search_by == 'Title':
    query = st.selectbox('Select Title:', book_data['Title'].unique())
else:
    query = st.selectbox('Select Author:', book_data['Authors'].unique())

# Set default value for number of recommendations from model
default_recommendations = 10

# User input to specify number of recommendations
n_recommendations = st.slider('Number of Recommendations', 1, 20, default_recommendations)

if st.button('Get Recommendations'):
    recommendations = get_recommendations_on_demand(query, search_by.lower(), n_recommendations)
    st.write(f'Recommendations for "{query}":')
    st.write(recommendations)


# Only use this section if 'Authors' is selected and the user has clicked 'Get Recommendations'
if search_by == 'Authors' and st.button(f'Get Books by {query}'):
    # Filter the DataFrame to get titles by the specific author selected from the dropdown
    books_by_author = book_data[book_data['Authors'] == query]['Title']

    # Check if any books were found
    if not books_by_author.empty:
        st.write(f'Books for "{query}":')
        for title in books_by_author:
            st.write(title)
    else:
        st.write(f'No books found for "{query}"')

# Example usage
if __name__ == '__main__':
    example_title = book_data['Title'].iloc[0]
    recommendations = get_recommendations_on_demand(example_title)
    print(recommendations)

