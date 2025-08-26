from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 4, 6, 7, 8, 9]

output_file("index.html")
source = ColumnDataSource(data=dict(x=x, y=y))
figure = figure()
figure.circle(x='x', y='y', size=10, source=source)
show(figure)
