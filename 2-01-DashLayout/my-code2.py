import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as graph_objs
import numpy as numpy

app = dash.Dash()

# Creating DATA
numpy.random.seed(42)
random_x = numpy.random.randint(1,101,100)
random_y = numpy.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure = {
                                     'data':[
                                         graph_objs.Scatter(
                                             x = random_x,
                                             y = random_y,
                                             mode = 'markers',
                                             marker = {
                                                 'size':12,
                                                 'color':'#2CA3CD',
                                                 'line':{'width':0.5}
                                             }
                                         )
                                     ],
                                     'layout':graph_objs.Layout(title='My Scatterplot',
                                                                xaxis = {'title':'X Title'})
                                     }
                                     ),
                        dcc.Graph(id='scatterplot2',
                                 figure = {
                                     'data':[
                                         graph_objs.Scatter(
                                             x = random_x,
                                             y = random_y,
                                             mode = 'markers',
                                             marker = {
                                                 'size':12,
                                                 'color':'#CD8B2C',
                                                 'line':{'width':0.5}
                                             }
                                         )
                                     ],
                                     'layout':graph_objs.Layout(title='Second Scatterplot',
                                                                xaxis = {'title':'X Title'})
                                     }
                                     )])


if __name__ == '__main__':
    app.run_server()
