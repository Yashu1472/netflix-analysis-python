
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('netflixproject.csv')

# Basic info
print(df.info())
print(df.describe())

# Number of movies and TV shows
print(df['type'].value_counts())

# Top 5 directors
print(df['director'].value_counts().head(5))

# Titles released in 2020
print("Titles released in 2020:", df[df['release_year'] == 2020].shape[0])

# Average movie duration
df['duration_int'] = df['duration'].str.extract('(\d+)').astype(float)
print("Average duration:", df['duration_int'].mean())

# Visualization: Count of type
sns.countplot(data=df, x='type')
plt.title('Count of Movies and TV Shows')
plt.show()
