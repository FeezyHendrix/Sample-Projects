from __future__ import division
import numpy as np

from bokeh.plotting import figure, HBox, VBox, output_file, show
from bokeh.models import Range1d

# Setting three different sets of data
x1 = [1, 2, 5, 7, -8, 5, 2, 7, 1, -3, -5, 1.7, 5.4, -5]
y1 = [5, 6, -3, 1.5, 2, 1, 1, 9, 2.4, -3, 6, 8, 2, 4]

x2 = np.random.random(size=100) * 20 - 10
y2 = np.random.random(size=100) * 20 - 10

x3 = [x for x in range(-5, 5)]
y3 = [x * 2 for x in range(-5, 5)]

# Naming an output file
output_file('scattering_points.html')

# Tools can be called upon in the figure function
TOOLS = "pan, wheel_zoom, box_zoom, reset, save"

# Setting a range for the graphs' axes
xr = Range1d(start=-10, end=10)
yr = Range1d(start=-10, end=10)

# Creating three different scatter plots
p1 = figure(x_range=xr, y_range=yr, tools=TOOLS, plot_width=500, plot_height=500)
p1.scatter(x1, y1, size=12, color="red", alpha=0.5)

p2 = figure(x_range=xr, y_range=yr, tools=TOOLS, plot_width=500, plot_height=500)
p2.scatter(x2, y2, size=12, color="blue", alpha=0.5, marker="square")

p3 = figure(x_range=xr, y_range=yr, tools=TOOLS, plot_width=500, plot_height=500)
p3.scatter(x3, y3, size=12, color="green", alpha=0.5, marker="triangle")

N = 4000  # Defining a size to be used in numpy functions

# Creating variables for a scatterplot based on random points
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5

# Creating random colors for the p4 scatter plot
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

# Creating a fourth scatter plot
p4 = figure(title="Colorful Scatter")
p4.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.5, line_color=None)

# Shows the first three plots in a horizontal plane with the final
# scatter plot in a vertical plane underneath
show(VBox(HBox(p1, p2, p3), p4))
