#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Plot real-world movie data from a CSV and save the plots.
# Usage: ./lab7f.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file from the correct raw GitHub URL
url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"

try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error reading or processing CSV file: {e}")
    exit()

# --- Create Plots ---
plt.figure(figsize=(15, 12))
plt.suptitle('IMDB Top 250 Movies Analysis', fontsize=20)

# Plot 1: Line plot of movie ratings over the years
plt.subplot(2, 2, 1)
df_sorted = df.sort_values('Year')
# CORRECTED LINE: Use 'IMDB rating' instead of 'Rating'
plt.plot(df_sorted['Year'], df_sorted['IMDB rating'])
plt.title('Movie Ratings Over the Years')
plt.xlabel('Year')
plt.ylabel('IMDB Rating') # Also updated the label for accuracy
plt.grid(True, linestyle='--', alpha=0.6)

# Plot 2: Bar plot of the number of movies per genre
# This part was already correct as it uses the 'Genre' column
plt.subplot(2, 2, 2)
genre_counts = df['Genre'].value_counts().nlargest(10)
genre_counts.plot(kind='bar')
plt.title('Top 10 Movie Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45, ha='right')

# Plot 3: Histogram of the number of movies per year
# This part was already correct as it uses the 'Year' column
plt.subplot(2, 2, 3)
plt.hist(df['Year'], bins=20, edgecolor='black')
plt.title('Distribution of Movie Release Years')
plt.xlabel('Year')
plt.ylabel('Number of Movies')

# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('lab7f_analysis_plots.png')
print("Analysis plots saved to lab7f_analysis_plots.png")