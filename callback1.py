from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the textbox to see callbacks in action"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
        ]),

    html.Br(),
    html.Div(id='my-output'),
    ])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
    )
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == "__main__":
    app.run_server(debug=True)
