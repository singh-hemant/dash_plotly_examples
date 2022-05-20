from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'India':['Delhi', 'Mumbai', 'Lucknow'],
    'America':['New York', 'San Francisco', 'Cincinnati']
}

app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'India',
        id='countries-radio',
        ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])

@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label':i, 'value':i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(av_options):
    return av_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(sel_country, sel_city):
    return u'{} is a city in {}.'.format(sel_city, sel_country)


if __name__ == "__main__":
    app.run_server(debug=True)
