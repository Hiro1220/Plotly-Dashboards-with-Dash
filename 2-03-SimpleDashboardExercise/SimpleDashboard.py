import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as graph_objs
import pandas as pandas


# read data set
df = pandas.read_csv('../Data/OldFaithful.csv')

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([dcc.Graph(id='old_faithful',
                                 figure={'data':[graph_objs.Scatter(x=df['X'],
                                                            y=df['Y'],
                                                            mode='markers')],
                                 'layout':graph_objs.Layout(title='Old Faithful Eruptions',
                                                            xaxis={'title':'Duration'
                                                            },
                                                            yaxis={'title':'Interval'})
                                 })])

if __name__ == '__main__':
    app.run_server()
    