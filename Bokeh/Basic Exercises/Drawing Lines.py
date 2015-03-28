from bokeh.plotting import figure, output_file, show, VBox, HBox

# Each item in the lists below represents a point on the graph
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [0, 8, 2, 4, 6, 9, 15, 18, 19, 25, 28]

x2 = range(4)
y2 = [x ** 2 for x in range(4)]

x3 = range(10)
y3 = [x * 3 for x in range(10)]

# Designates what to name the output file
output_file("drawing_lines.html")

# Creates a plot for each list and modifies the graph's line
p1 = figure(plot_width=500, plot_height=500, background_fill="ghostwhite")
p1.line(x1, y1, size=5, color='red', alpha=1, line_width=3)

p2 = figure(plot_width=500, plot_height=500, background_fill="ghostwhite")
p2.line(x2, y2, size=15, color='black', alpha=1, line_width=2)

p3 = figure(plot_width=500, plot_height=500, background_fill="ghostwhite")
p3.line(x3, y3, size=30, color="grey", alpha=1, line_width=1)

# Creates a plot that combines all other plots
p4 = figure(title="Combo", background_fill="ghostwhite")
p4.line(x1, y1, size=5, color='red', alpha=1, line_width=3)
p4.line(x2, y2, size=15, color='black', alpha=0.5, line_width=2)
p4.line(x3, y3, size=30, color="grey", alpha=0.75, line_width=1)

# Shows the first three plots in a horizontal plane
# and the final plot in a vertical plane underneath
show(VBox(HBox(p1, p2, p3), p4))
