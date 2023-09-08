# -*- coding: utf-8 -*-
"""
Created on 2022/10/11

@author: Caixia Tian
"""

from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask, send_from_directory

app = Dash(
    __name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP, 
        dbc.icons.BOOTSTRAP
    ],
    suppress_callback_exceptions=True,
)

# 设置网页title
app.title = 'GCTADD-Tool'

server = app.server # app.server 上提供了底层 Flask 应用程序。