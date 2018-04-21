# -*- coding: utf-8 -*-

# TODO: tirar index de tempo e fazer uma coluna separada (ou talvez não)ls

import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

app = dash.Dash()

df = pd.read_csv('~/Downloads/teste.csv')

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

#RangeSlider
#https://dash.plot.ly/getting-started-part-2

dcc.RangeSlider(
    min = 0,
    max = 7,
    step = None,
    marks = {
        0: '8Hrs',
        1: '5Hrs',
        2: '2Hrs',
        3: '1Hr',
        4: '30min',
        5: '15min',
        6: '5min',
        7: 'Agora'
    },
    value = [6, 7]
)



@call.callback(

)

def update_graph(

)

if __name__ == '__main__':
    app.run_server(debug=True)