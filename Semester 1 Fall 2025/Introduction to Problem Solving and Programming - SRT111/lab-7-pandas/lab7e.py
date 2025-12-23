#!/usr/bin/env python3
# Author: Soroush Bastani (SBastani1)
# Date: 2025-11-07
# Purpose: Arrange multiple plots in subplots and save the figure.
# Usage: ./lab7e.py

import matplotlib
matplotlib.use('Agg') # Set non-GUI backend
import matplotlib.pyplot as plt

# 1. Data for four different plots
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 3, 6, 2, 7]
y4 = [10, 8, 6, 4, 2]

# 2. Create a figure to hold the subplots
plt.figure(figsize=(10, 8))
plt.suptitle('Comparison of Four Plots', fontsize=16)

# 3. Create subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue')
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='green')
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot(x, y3, color='red')
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot(x, y4, color='purple')
plt.title("Plot 4")

# 4. Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust for suptitle

# 5. Save the entire figure
plt.savefig('lab7e_subplots.png')
print("Subplots figure saved to lab7e_subplots.png")