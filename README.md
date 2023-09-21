# AI-detecting-plagarism-of-different-texts-in-percentage

**Plagiarism Detection using Cosine Similarity**

This Python script is designed to detect plagiarism by calculating the cosine similarity between a user's input document and a list of descriptions from a database. It serves as a basic plagiarism checker and can be a starting point for more advanced implementations.

**Features:**

- Utilizes the NLTK library for natural language processing.
- Implements cosine similarity as the similarity metric.
- Reads the user's input document and a list of descriptions from a database.
- Tokenizes text and calculates word frequency vectors.
- Compares the user's input with each description to find the highest similarity score.
- Presents the highest similarity score as a percentage.

**Usage:**

1. Run the script and provide your document for comparison when prompted.
2. The script will compare your document with each description in the database.
3. It will display the highest similarity score as a percentage, indicating the level of similarity between your document and the most similar description in the database.

Feel free to customize the `database_descriptions` list with actual descriptions from your database to perform real-world plagiarism checks.
