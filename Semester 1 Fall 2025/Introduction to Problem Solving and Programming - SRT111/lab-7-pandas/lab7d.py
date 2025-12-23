#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Generate and save a bar chart and a histogram.
# Usage: ./lab7d.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import matplotlib.pyplot as plt

# --- Part 1: Bar Chart ---

# 1. Data for bar chart
products = ['Coffee', 'Tea', 'Juice', 'Soda']
sales = [150, 120, 90, 60]

# 2. Create and save the bar chart
plt.figure(1)
plt.bar(products, sales)
plt.title('Product Sales')
plt.xlabel('Product Category')
plt.ylabel('Sales (Units)')
plt.savefig('lab7d_barchart.png')
print("Bar chart saved to lab7d_barchart.png")

# --- Part 2: Histogram ---

# 3. Data for histogram
daily_sales = [20, 15, 25, 18, 30, 12, 22, 28, 16, 14, 19, 21]

# 4. Create and save the histogram
plt.figure(2)
plt.hist(daily_sales, bins=5, edgecolor='black')
plt.title('Distribution of Daily Sales')
plt.xlabel('Daily Sales')
plt.ylabel('Frequency (Number of Days)')
plt.savefig('lab7d_histogram.png')
print("Histogram saved to lab7d_histogram.png")