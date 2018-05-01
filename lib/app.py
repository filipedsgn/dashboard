#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: tirar index de tempo e fazer uma coluna separada (ou talvez não)ls


import dash
import pandas as pd
import os

from lib import config, graficos
from flask import send_from_directory

import plotly.plotly as py
from plotly.graph_objs import *
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import send_from_directory
import os

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Link(rel='stylesheet', href='/static/stylesheet.css'),
    html.Div(children="Residência", className="header"),
    html.Div(children=grafico_linha('Temperatura'), className="grafico1"),
    html.Div(children=grafico_linha('Humidade'), className="grafico2"),
    html.Div(children=grafico_linha('Luminosidade'), className="grafico3")
], className="wrapper")


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


if __name__ == '__main__':
    app.run_server()
