from dash import Dash, dcc, html, Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='ip-1', type='text', value='Delhi'),
    dcc.Input(id='ip-2', type='text', value='India'),
    html.Button(id='submit', n_clicks=0, children='Submit'),
    html.Div(id='number-output'),
    ])

@app.callback(
    Output('number-output', 'children'),
    Input('submit', 'n_clicks'), 
    State('ip-1', 'value'),
    State('ip-2', 'value'))
def update_output(n_clicks, ip1, ip2):
    return u'Input 1 id {} and Input 2 is {}.'.format(ip1, ip2)


if __name__ =="__main__":
    app.run_server(debug=True)
