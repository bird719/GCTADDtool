# -*- coding: utf-8 -*-
"""
Created on 2023/8/29

@author: Tina
"""

import sys
import os
import shutil
import pandas as pd
from urllib.parse import quote as urlquote
import plotly.express as px
import dash_uploader as du
import dash_bootstrap_components as dbc
from pathlib import Path
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
from server import app
from pages.subs.db_tools import generate_datatable,blast_tools,predict_tool


folder = Path(__file__).parent /'tmp'
du.configure_upload(app, str(folder))

project_initial = 'Import the object so that Dash can scan corresponding callback functions when packaging applications'

@app.callback(
    Output("blast-card1", "is_open"),
    [Input("blast-button1", "n_clicks")],
    [State("blast-card1", "is_open")],
)
def display_blastinfo(n, is_open):
    if n:
        return not is_open
    return is_open


#Blast Page
@app.callback(
    Output("output1", "children"), 
    Input("blast_type", "value"),
    Input("blast_upload","value"),
    Input('blast_upload', 'isCompleted'),
    Input("blast_button","n_clicks"),
    State('blast_upload', 'fileNames'),
    State('blast_upload', 'upload_id'),
    prevent_initial_call=False,
)
def out_blastlog(blast_type,blast_upload,is_completed,b_clicks,filenames,upload_id):
    if is_completed and b_clicks:
        tfilename = filenames[0]   
        filepath = folder / upload_id / tfilename
        filepath = os.path.normpath(filepath)
        print(filepath)
        filename = blast_tools(blast_type,filepath)
        ofilename = filename[0].split('/')[-1]  #for Linux
        return html.Div(
            [
                dbc.Row(
                    dbc.Alert(
                        [
                            html.I(className="bi bi-check-circle-fill me-2"),
                            "Sequence blast has completed !",
                        ],
                        id="blast_stat",
                        color="success",
                        className="d-flex align-items-center",
                    ),
                ),
                html.Br(),
            ]
        )

@app.callback(
    Output("blast_download", "data"),
    Input('blast_upload', 'isCompleted'),
    Input("blast_button", "n_clicks"),
    Input("blast_output","n_clicks"),
    State('blast_upload', 'fileNames'),
    State('blast_upload', 'upload_id'),
    prevent_initial_call=False,
)
def out_blastfile(isCompleted,n_clicks,d_clicks,filenames,upload_id):
    if isCompleted and n_clicks:
        if d_clicks:
            tfilename = filenames[0]   
            filepath = folder / upload_id / tfilename
            filepath = os.path.normpath(filepath)
            filename = filepath.split('.')[0]  #for Linux
            ofilename = os.path.normpath(filename + '.txt')
            print(ofilename)
            if os.path.exists(ofilename):
                print('ok')
                return dcc.send_file(ofilename)
            else:
                print('error')


# ACP/AMP Predict Page analysis
@app.callback(
    Output("output2", "children"), 
    Input("radioItem2", "value"),
    Input('predict_upload1', 'isCompleted'),
    Input('predict_upload2','isCompleted'),
    Input("predict_button2","n_clicks"),
    State('predict_upload1', 'fileNames'),
    State('predict_upload1', 'upload_id'),
    State('predict_upload2', 'fileNames'),
    State('predict_upload2', 'upload_id'),
    prevent_initial_call=False,
)
def out_predictlog(type2,is_completed1,is_completed12,b_clicks,filenames1,upload_id1,filenames2,upload_id2):
    if is_completed1 and b_clicks:
        tfilename = filenames1[0]   
        filepath = folder / upload_id1 / tfilename
        filepath = os.path.normpath(filepath)
        print(filepath)
        if is_completed12:
            pssm_filename = filenames2[0]
            pssm_filepath = folder / upload_id2 / pssm_filename
            pssm_filepath = os.path.normpath(pssm_filepath)
            print(pssm_filepath)
        else:
            pssm_filepath = blast_tools('psiblast',filepath)
        
        outfiles = predict_tool(type2,filepath,pssm_filepath)
        outdata1 = pd.read_csv(outfiles[0])
        if len(outfiles) == 2:
            outdata2 = pd.read_csv(outfiles[1])
        return html.Div(
            [
                dbc.Alert(
                    [
                        html.I(className="bi bi-check-circle-fill me-2"),
                        "ACP/AMP predict has completed !",
                    ],
                    color="success",
                    className="d-flex align-items-center",
                ),
                html.Br(),
                generate_datatable(outdata1),
                generate_datatable(outdata2) if len(outfiles) == 2 else html.Br()
            ]
        )

# ACP/AMP Predict Page example
@app.callback(
    Output("output3", "children"),
    Input("radioItem2", "value"),
    Input('example_button','n_clicks'),
    prevent_initial_call=False,
)
def out_predictexample(type3,n_clicks3):
    acp_example = '/gctadd-tool/pages/subs/TriNet/acpout.csv'
    amp_example = '/gctadd-tool/pages/subs/TriNet/ampout.csv'
    outlist = ['1']
    if n_clicks3:
        if type3 == 'ACP':
            outdata = pd.read_csv(acp_example)
        elif type3 == 'AMP':
            outdata = pd.read_csv(amp_example)
        elif type3 == 'ALL':
            outlist.append('2')
            outdata = pd.read_csv(acp_example)
            outamp = pd.read_csv(amp_example)
        return html.Div(
            [
                dbc.Alert(
                    [
                        html.I(className="bi bi-check-circle-fill me-2"),
                        "ACP/AMP predict has completed !",
                    ],
                    color="success",
                    className="d-flex align-items-center",
                ),
                html.Br(),
                generate_datatable(outdata),
                generate_datatable(outamp) if len(outlist) == 2 else html.Br()
            ]
        )

