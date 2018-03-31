# -*- coding: utf-8 -*-

# TODO: tirar index de tempo e fazer uma coluna separada (ou talvez não)

import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

app = dash.Dash()

df = pd.read_csv('~/Downloads/teste.csv')

'''
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
'''

app.layout = html.Div([
    dcc.Graph(
        id='dados-sensoriais',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['bla'] == i]['temp'],
                    y=df[df['bla'] == i]['']
                )
            ]
        }
    )
])

if __name__ == '__main__':
    #adicionado estilo css
    app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
    app.run_server(debug=True)

    https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv