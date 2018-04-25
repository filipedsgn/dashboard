#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: tirar index de tempo e fazer uma coluna separada (ou talvez não)ls


import dash
import pandas as pd

from lib import config

app = dash.Dash()

df = pd.read_csv(config.ARQ['dados']).tail(360)



# tudo
app.layout = html.Div([
    # header
    html.Div(['----HEADER----'], style={'width': '98%', 'display': 'inline-block'}),
    # conteúdo
    html.Div([
        # graf temp
        html.Div(['----GRAFICO TEMP----'], style={}),
        # barra horizontal
        html.Div(['----BARRA HORIZONTAL----'], style={}),
        # conteúdo 2
        html.Div(['----DIV----'
                  # gráfico humidade
                  html.Div(['----GRAFICA HUMI----'], style={}),
                  # barra vertical
                  html.Div(['----BARRA VERTICAL----'], style={}),
                  # gráfico luminosidade
                  html.Div(['----GRAFICO LUMI----'], style={}),
                 )], style={}
    )], style={})
], style={'borderBottom': 'thin lightgrey solid', 'backgroundColor': 'rgb(250,250,250)', 'padding': '10px 5px'})

if __name__ == '__main__':
    app.run_server()