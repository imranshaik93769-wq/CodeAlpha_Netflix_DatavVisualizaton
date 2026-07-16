import pandas as pd
## Load the Netflix dataset
df=pd.read_csv('netflix_titles.csv')
## Display the first few rows of the dataset
print(df.head())

print("\nShape of the dataset:", df.shape)

print("\nColumns in the dataset:", df.columns)

print("\nData Information:\n", df.info())

print("\nstatistical Summary:\n", df.describe())

print("\nMissing Values in each column:\n", df.isnull().sum())

print("\nDuplicate rows in the dataset:", df.duplicated().sum())

print("\nRemove the rows with missing values:",df.dropna(inplace=True))
print("\nMissing values after cleaning:",df.isnull().sum())

print("\nRows before removing duplicates:", len(df))
print("\nRows after removing duplicates:", len(df.drop_duplicates()))

df.to_csv('cleaned_netflix.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_netflix.csv'")
print("\nDataset saved successfully")

##insights from the dataset

#1) The count of movies and TV shows of Netflix.
print("\nMovies vs TV Shows")
print(df["type"].value_counts())

#2) The top 10 countries with the highest number of Netflix titles.
print("\nTop 10 Countries")
print(df["country"].value_counts().head(10))

#3) The Content rating of Netflix.
print("\nContent Ratings")
print(df["rating"].value_counts())

#4) The top 10 release years of Netflix.
print("\nTop 10 Release Years")
print(df["release_year"].value_counts().head(10))

#5) the top Generes of Netflix.
print("\nTop 10 Genres")
print(df["listed_in"].value_counts().head(10))

##Visualization for insights
#1) Movies vs TV Shows
import pandas as pd
import matplotlib.pyplot as plt

# Load Cleaned Dataset
df = pd.read_csv("cleaned_netflix.csv")

# Count Movies and TV Shows
type_count = df["type"].value_counts()

# Create Bar Chart
plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values)

# Title and Labels
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")

# Save Chart
plt.savefig("output/movies_vs_tvshows.png")

# Display Chart
plt.show()

#2) Top 10 Countries with the highest number of Netflix titles
# Top 10 Countries
country_count = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.bar(country_count.index, country_count.values)

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/top10_countries.png")

plt.show()

#3) Content Ratings of Netflix
# Content Ratings Pie Chart
rating_count = df["rating"].value_counts().head(6)

plt.figure(figsize=(7,7))

plt.pie(
    rating_count.values,
    labels=rating_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Content Ratings Distribution")

plt.savefig("output/content_ratings_pie.png")

plt.show()

#4) Top 10 Release Years of Netflix
# Release Year Histogram

plt.figure(figsize=(10,5))

plt.hist(df["release_year"], bins=20)

plt.title("Distribution of Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.savefig("output/release_year_histogram.png")

plt.show()

#5) Top 10 Genres of Netflix
# Top 10 Genres

genre_count = df["listed_in"].value_counts().head(10)

plt.figure(figsize=(12,6))

plt.bar(genre_count.index, genre_count.values)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Shows")

plt.xticks(rotation=60)

plt.tight_layout()

plt.savefig("output/top10_genres.png")

plt.show()