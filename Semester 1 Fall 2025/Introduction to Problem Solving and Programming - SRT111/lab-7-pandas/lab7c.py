#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Create a scatter plot and save it to a file.
# Usage: ./lab7c.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import matplotlib.pyplot as plt

# 1. Data points
x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# 2. Create a scatter plot with customizations
plt.scatter(x, y, c='green', s=100, alpha=0.6)

# 3. Add titles and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')

# 4. Save the plot to a file
plt.savefig('lab7c_plot.png')
print("Plot saved to lab7c_plot.png")