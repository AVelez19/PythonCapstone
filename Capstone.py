import matplotlib.pyplot as plt
import numpy as np

'''
Generate random data
Color of each point
Create scatter plot
Set figure size (width, height)
Set is marker size, alpha is transparency
Add color bar indicating the scale of the color
Enable grid
'''

np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)


plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=100, c=colors, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')
plt.grid(True)
plt.show()
