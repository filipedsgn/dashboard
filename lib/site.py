#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import graficos

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
    html.Div(children=graficos.linha('Temperatura'), className="g1"),
    html.Div(children=graficos.linha('Humidade'), className="g2"),
    html.Div(children=graficos.linha('Luminosidade'), className="g3")
], className="wrapper")


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


app.run_server(port=8050, host='0', debug=True)
