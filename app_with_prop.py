from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                 'Fertility rate, total (births per woman)',
                id='xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width':'48%', 'display':'inline-block'}),

        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Life expectancy at birth, total (years)',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width':'48%', 'display':'inline-block', 'float':'right'})
    ]),

    dcc.Graph(id="indicator-graphic"),

    dcc.Slider(
        df['Year'].min(),
        df['Year'].max(),
        step=None,
        id='year--slider',
        value=df['Year'].max(),
        marks = {str(year):str(year) for year in df['Year'].unique()},
    )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'))


def update_graph(xa_cn, ya_cn, xa_type, ya_type, year_value):
    dff = df[df['Year']==year_value]

    fig = px.scatter(x=dff[dff['Indicator Name']==xa_cn]['Value'],
                     y=dff[dff['Indicator Name']==ya_cn]['Value'],
                     hover_name=dff[dff['Indicator Name']==ya_cn]['Country Name'])

    fig.update_layout(margin={'l':40, 'b':40, 't':10, 'r':0}, hovermode='closest')

    fig.update_xaxes(title=xa_cn, type='linear' if xa_type=='Linear' else 'log')

    fig.update_yaxes(title=ya_cn, type='linear' if ya_type=='Linear' else 'log')

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)











    
    
