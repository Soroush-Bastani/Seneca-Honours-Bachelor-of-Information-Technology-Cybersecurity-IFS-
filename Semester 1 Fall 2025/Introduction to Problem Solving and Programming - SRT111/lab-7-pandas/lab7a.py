#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Create a simple line plot and save it to a file.
# Usage: ./lab7a.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import matplotlib.pyplot as plt

# 1. Data lists
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Plot y versus x
plt.plot(x, y)

# 3. Add titles and labels for clarity
plt.title('My First Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# 4. Save the plot to a file
plt.savefig('lab7a_plot.png')
print("Plot saved to lab7a_plot.png")