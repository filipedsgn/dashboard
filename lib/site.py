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

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Link(rel='stylesheet', href='/static/stylesheet.css'),
    html.Div(children="Residência", className="header"),
    html.Div(children=graficos.linha('Temperatura'), className="g1"),
    html.Div(children=graficos.linha('Umidade'), className="g2"),
    html.Div(children=graficos.linha('Luminosidade'), className="g3")
], className="wrapper")


@app.server.route('/static/<resource>')
    def serve_static(resource):
        return flask.send_from_directory(STATIC_PATH, resource)


app.run_server(port=8050, host='0', debug=True)

'''
import flask    
import os



'''

'''
Here’s a slightly easier way… if you have a CSS file in assets/main.css then you can use the static_folder argument of dash.Dash() to serve up that folder, and then use html.Link to reference it, with an href that starts with / to make it relative to the root of your server:

app = dash.Dash(__name__, static_folder='assets')
app.scripts.config.serve_locally=True
app.css.config.serve_locally=True
app.layout = html.Div([
    html.Link(href='/assets/main.css', rel='stylesheet'),
    .....
])
'''