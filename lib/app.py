#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: tirar index de tempo e fazer uma coluna separada (ou talvez não)ls


import dash
import pandas as pd

from lib import config, graficos

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        html.Div([
            html.Div(['Residência'], style={'fontSize': '22.4px', 'fontWeight': '200', 'marginLeft': '22.4px', 'lineHeight': '3em', 'display': 'block', 'lineWeight': '200', 'boxSizing': 'border-box'})
            ], style={}
        ),
        html.Div([
            html.Div(children=grafico_linha('Temperatura'), style={}),
            html.Div([], style={}),
            html.Div([
                html.Div(children=grafico_linha('Humidade'), style={}),
                html.Div([], style={}),
                html.Div(children=grafico_linha('Extra'), style={})
                ])
            ])
        ])
    )
if __name__ == '__main__':
    app.run_server()