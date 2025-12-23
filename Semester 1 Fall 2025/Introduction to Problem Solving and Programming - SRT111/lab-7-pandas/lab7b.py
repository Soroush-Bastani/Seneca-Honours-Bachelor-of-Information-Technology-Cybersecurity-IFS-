#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Plot multiple lines on the same figure and save it.
# Usage: ./lab7b.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import matplotlib.pyplot as plt

# 1. Data for two lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# 2. Plot both lines with customizations
plt.plot(x, y1, color='blue', linestyle='-', label='y = 2x')
plt.plot(x, y2, color='red', linestyle='--', label='y = x^2')

# 3. Add titles and labels
plt.title('Comparing Two Lines')
plt.xlabel('X Values')
plt.ylabel('Y Values')

# 4. Add a legend and grid
plt.legend()
plt.grid(True)

# 5. Save the plot to a file
plt.savefig('lab7b_plot.png')
print("Plot saved to lab7b_plot.png")