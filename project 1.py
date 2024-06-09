Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import matplotlib.pyplot as plt
... 
... # Load the dataset
... df = pd.read_csv('movie_ratings.csv')
... 
... # Clean the data
... df.dropna(inplace=True)
... df['rating'] = df['rating'].astype(float)
... 
... # Perform basic analysis
... average_ratings = df.groupby('movie_title')['rating'].mean().reset_index()
... 
... # Visualize the results
... plt.figure(figsize=(10, 5))
... plt.bar(average_ratings['movie_title'], average_ratings['rating'], color='skyblue')
... plt.xlabel('Movie Title')
... plt.ylabel('Average Rating')
... plt.title('Average Movie Ratings')
... plt.xticks(rotation=90)
... plt.show()
