from flask import Flask, render_template
import plotly.graph_objs
import plotly.offline

flask = Flask(__name__)

# The first page should display a bar or pie chart created 
# using Python. I don't care what this chart shows.
@flask.route('/bar')
def chart1():
    data = [ plotly.graph_objs.Bar(
            x=['a', 'b', 'c', 'd'],
            y=[1, 2, 3, 4]
        )
    ]

    figure = plotly.graph_objs.Figure(data=data)
    chart = plotly.offline.plot(figure, output_type='div')
    return render_template('chart1.html', chart=chart)

# The second page should display a line chart created using Python.  
# I don't care what this chart shows either but it should be
# different data than the first chart.
@flask.route('/line')
def chart2():
    data = [ plotly.graph_objs.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )
    ]

    figure = plotly.graph_objs.Figure(data=data)
    chart = plotly.offline.plot(figure, output_type='div')
    return render_template('chart2.html', chart=chart)

if __name__ == '__main__':
    flask.run(debug=True)
