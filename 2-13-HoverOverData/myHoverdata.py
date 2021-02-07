import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as graph_objs
import pandas as pandas
import json
import base64

app = dash.Dash()

df = pandas.read_csv('../Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
                       html.Div(dcc.Graph(id='wheels-plot',
                                          figure={'data':[graph_objs.Scatter(
                                                                x=df['color'],
                                                                y=df['wheels'],
                                                                dy=1,
                                                                mode='markers',
                                                                marker={'size':15}
                                                  )],
                                                  'layout':graph_objs.Layout(title='Test',
                                                                             hovermode='closest')
                                                 }
                                          ),
                                 style={'width':'30%','float':'left'}
                                ),
                       #Output Area
                       html.Div([html.Img(id='hover-data', src='children', height=300)],
                                style={'[addingTop]':'35%'}
                                )
])

@app.callback(Output('hover-data','src'),
              [Input('wheels-plot','clickData')]) # hoverData is a property of plotly: https://dash.plotly.com/interactive-graphing
def callback_image(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = '../Data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ =='__main__':
    app.run_server()
