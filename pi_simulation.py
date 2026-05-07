import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import pandas as pd

fig, ax = plt.subplots()

square = patches.Rectangle((-1, -1), 2, 2, linewidth=2, edgecolor='blue', facecolor='none')
circle = patches.Circle((0, 0), 1, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(square)
ax.add_patch(circle)

ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

x_in, y_in = [], []
x_out, y_out = [], []

# Create two scatter objects (one for each category)
# s=5 controls the size of the dots
scatter_in, = ax.plot([], [], 'o', color='red', markersize=3, label='Inside')
scatter_out, = ax.plot([], [], 'o', color='blue', markersize=3, label='Outside')

# 3. Update function
def update(frame):
    # Generate a random point
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    
    # Check if point is inside the unit circle
    if x**2 + y**2 <= 1:
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)
    
    # Update the data for both scatter plots
    scatter_in.set_data(x_in, y_in)
    scatter_out.set_data(x_out, y_out)
    total = len(x_in) + len(x_out)
    pi_est = 4 * len(x_in) / total if total > 0 else 0
    ax.set_title(f"Points: {total} | Inside: {len(x_in)} | Outside: {len(x_out)} | π ≈ {pi_est:.4f}")
    
    # Return the artists that changed
    return scatter_in, scatter_out




ani = FuncAnimation(fig, update, frames=500, blit=False, interval=50)

#ani.save('animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
ani.save("animation.gif", writer="pillow", fps=30)
plt.show()