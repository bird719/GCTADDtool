# -*- coding: utf-8 -*-
"""
Created on 2023/08/22

@author: Tina
"""

import base64
import os
from pydoc import classname

import shutil
import pandas as pd
from pathlib import Path
from dash import Dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_uploader as du
from dash.dependencies import Input, Output

from server import app
from pages.Home import home_page
from pages.blast import blast_page
from pages.predict import predict_page
from pages.resource import resources_page
from pages.help import help_page


APP_PATH = str(Path(__file__).parent.resolve())



# 标题栏+菜单栏
light_logo=True
app_title="GCTADD Tool"
app_name="GCTADD"
bg_color="#0D1A51"
font_color="#F3F6FA"
bar_top=html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    
                    dbc.Col(
                        [
                            html.A(
                                'dash app',
                                style={
                                    'color':bg_color
                                }
                            ),
                            html.H2(
                                app_title,
                            ),
                            html.Img(
                                src=app.get_asset_url(
                                    "GitHub-Mark-Light-64px.png"
                                ),
                            ),
                            html.A(
                                id='gh-link',
                                children=[
                                    'View on GitHub'
                                ],
                                href="https://github.com/bird719/GCTADDtool",
                                style={'color': 'white' if light_logo else 'black',
                                    'border': 'solid 1px white' if light_logo else 'solid 1px black'
                                }
                            ), 
                        ],
                        width=12,
                        class_name='app-page-header'
                    ),
                    dbc.Col(
                        [
                            html.Label(
                                "A tool website for guiding cancer treatment and antibiotic drug design.",
                                style={
                                    "color":"white",
                                    "margin-top": "3.2rem",
                                    "margin-left": "4.4rem",
                                }
                            ),
                        ],
                        width=12
                    ),
                    dbc.Col(
                        [
                        ],
                        width=7,
                    ),
                    dbc.Col(
                        [
                            dbc.Nav(
                                [
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            'HOME', 
                                            active='exact', 
                                            href='/',
                                            class_name='nav-item'
                                        ),
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            'BLAST',
                                            active='exact',
                                            href='/Blast',
                                            class_name='nav-item'
                                        ),
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            'PREDICT ACP/AMP',
                                            active='exact',
                                            href='/Predict',
                                            class_name='nav-item'
                                        )
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            'RESOURCES',
                                            active='exact',
                                            href='/Resoures',
                                            class_name='nav-item'
                                        )
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            'HELP',
                                            active='exact',
                                            href='/Help',
                                            class_name='nav-item'
                                        )
                                    ),
                                ]
                            )
                        ],
                        align='right',
                        width=5,
                    )
                ],
                justify="between",
                style={
                    'background': bg_color,
                    'color': font_color,
                    'height':'8rem'
                }
            ),    
        ],
        fluid=True,
    ),
)


# 页面内容
content = html.Div(id="page-content", className='page-all')

# 底部栏
bar_bottom = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        'Contact: tina@dash.com', width=12,
                        class_name='bar-bottom-text',
                    ),
                ],
                align='center',
                class_name='bar-bottom',
            ),
        ],
        fluid=True,
    ),
)

app.layout = html.Div(
    [
        dcc.Location(id='url'),
        bar_top, 
        content,
        bar_bottom
    ],
)
       
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')],
)
def render_page_content(pathname):
    if pathname == '/':
        return home_page
    if pathname == '/Home':
        return home_page
    elif pathname == '/Blast':
        return blast_page
    elif pathname == '/Predict':
        return predict_page
    elif pathname == '/Resoures':
        return resources_page
    elif pathname == '/Help':
        return help_page
    return html.Div('No such page !')

if __name__ == "__main__":
    app.run_server(debug=True)
