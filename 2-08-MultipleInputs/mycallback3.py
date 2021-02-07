import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as graph_objs
import pandas as pandas

df = pandas.read_csv('../Data/mpg.csv')

app = dash.Dash()

# Creating a list of options
features = df.columns

app.layout = html.Div([
                      #1st Dropdown
                      html.Div([
                        dcc.Dropdown(
                            id='xaxis',
                            options=[{'label':i,'value':i} for i in features],
                            value='displacement'
                        )
                      ],style={'width':'45%','display':'inline-block'}),
                      #2nd Dropdown
                      html.Div([
                          dcc.Dropdown(
                              id='yaxis',
                              options=[{'label':i,'value':i} for i in features],
                              value='mpg'
                          )
                      ],style={'width':'45%','display':'inline-block'}),
                      #Graph
                      dcc.Graph(id='feature-graphic')
],style={'padding':10})

@app.callback(Output('feature-graphic','figure'),
              [Input('xaxis','value'),
               Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):
    return {'data':[graph_objs.Scatter(
                            x=df[xaxis_name],
                            y=df[yaxis_name],
                            text=df['name'],
                            mode='markers',
                            marker={'size':15,
                                    'opacity':0.5,
                                    'line':{'width':0.5,'color':'white'}
                                    }
                    )],
            'layout':graph_objs.Layout(title='My Dashboard for MPG',
                                   xaxis={'title':xaxis_name},
                                   yaxis={'title':yaxis_name},
                                   hovermode='closest')
            }

if __name__ == '__main__':
    app.run_server()
