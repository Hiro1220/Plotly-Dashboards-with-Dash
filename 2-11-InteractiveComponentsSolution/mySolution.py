import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
                      dcc.RangeSlider(
                          id='range-slider',
                          min=-10,
                          max=11,
                          step=1.0,
                          marks={i:str(i) for i in range(-10,11)},
                          value=[-1,1]
                          ),
                      html.H1(id='result-container')
                     ],
                     style={'fontFamily':'Helvetica','fontsize':18})

@app.callback(Output('result-container','children'),
              [Input('range-slider','value')])
def calculate_result(value_list):
    result = value_list[0] * value_list[1]
    return "Multiplication of your choice is: {}".format(result)

if __name__ == '__main__':
    app.run_server()
