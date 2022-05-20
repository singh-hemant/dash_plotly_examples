from dash import Dash, html, dcc

app = Dash(__name__)

markdown_text = '''
    ### Dash and Markdown

    Dash apps can be written in Markdown.
    
    Dash uses the [CommonMark](#).
    
    specification of markdown.
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
    ])


if __name__ == "__main__":
    app.run_server(debug=False)
