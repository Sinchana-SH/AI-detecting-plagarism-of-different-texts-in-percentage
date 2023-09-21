import nltk
import math
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

# Function to calculate cosine similarity between 2 vectors
def cosine_similarity(a, b):
    numerator = sum([a[i] * b[i] for i in range(len(a))])
    denominator = math.sqrt(sum([a[i] ** 2 for i in range(len(a))])) * math.sqrt(sum([b[i] ** 2 for i in range(len(b))]))
    return (numerator / denominator) * 100  # Multiply by 100 to get the result in percentage

# Read the user's input document
user_input = input("Enter your document: ")

# List of descriptions from the database (you can replace this with your database retrieval logic)
database_descriptions = [
    "Description 1 from the database",
    "Description 2 from the database",
    "Description 3 from the database",
]

highest_similarity = 0  # Initialize the highest similarity score

# Tokenize the user input
user_tokens = [word.lower() for word in word_tokenize(user_input) if word.isalpha()]

for description in database_descriptions:
    # Tokenize the database description
    description_tokens = [word.lower() for word in word_tokenize(description) if word.isalpha()]

    # Calculate the frequency of the words in each token list
    freq_user = Counter(user_tokens)
    freq_description = Counter(description_tokens)

    # Create a set of unique words across both documents
    unique_words = set(list(freq_user.keys()) + list(freq_description.keys()))

    # Calculate the frequency vectors for each document
    vector_user = [freq_user[word] if word in freq_user else 0 for word in unique_words]
    vector_description = [freq_description[word] if word in freq_description else 0 for word in unique_words]

    # Calculate the cosine similarity between the two vectors
    similarity_score = cosine_similarity(vector_user, vector_description)

    # Update the highest similarity if a higher similarity is found
    if similarity_score > highest_similarity:
        highest_similarity = similarity_score

# Print out the highest similarity score as a percentage
print(f"The similarity with other texts is {round(highest_similarity, 2)}%")
