#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Annotate key data points on a plot and save the figure.
# Usage: ./lab7g.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file
url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit()

# Sort data by year for a clean line plot
df = df.sort_values('Year')

# 2. Create the line plot
plt.figure(figsize=(14, 8))
# CORRECTED LINE: Use 'IMDB rating' instead of 'Rating'
plt.plot(df['Year'], df['IMDB rating'], linestyle='--', marker='o', alpha=0.5, label='All Movies')

# 3. Highlight key points
# CORRECTED LINES: Use 'IMDB rating' to find the max rating
highest_rating_movie = df.loc[df['IMDB rating'].idxmax()]
earliest_movie = df.loc[df['Year'].idxmin()]
latest_movie = df.loc[df['Year'].idxmax()]

# Mark these points on the plot
plt.scatter(highest_rating_movie['Year'], highest_rating_movie['IMDB rating'], color='red', s=120, zorder=5, label='Highest Rating')
plt.scatter(earliest_movie['Year'], earliest_movie['IMDB rating'], color='green', s=120, zorder=5, label='Earliest Movie')
plt.scatter(latest_movie['Year'], latest_movie['IMDB rating'], color='purple', s=120, zorder=5, label='Latest Movie')

# 4. Annotate the highest-rated movie
plt.annotate(
    f"{highest_rating_movie['Title']} ({highest_rating_movie['IMDB rating']})",
    xy=(highest_rating_movie['Year'], highest_rating_movie['IMDB rating']),
    xytext=(highest_rating_movie['Year'] - 20, highest_rating_movie['IMDB rating'] - 0.1),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8)
)

# 5. Add titles, labels, and legend
plt.title('IMDB Top 250 Movie Ratings by Year with Annotations')
plt.xlabel('Year')
plt.ylabel('IMDB Rating') # Also updated the label for accuracy
plt.legend()
plt.grid(True)

# 6. Save the figure to a file
plt.savefig("lab7g_annotated_plot.png")
print("Annotated plot saved to lab7g_annotated_plot.png")