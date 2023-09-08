import sys
import pandas as pd
from http.client import OK
from dash import html, dcc,Input, Output
import dash_bootstrap_components as dbc
import dash_uploader as du
from callbacks.allrun import project_initial


title_top_search = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src='/assets/ctadd-blast-icon-1.png', 
                            className='img-style2'
                        ),
                        width=1,
                    ),
                    dbc.Col(
                        'Basic Local Alignment Search Tool',
                        style={
                            'margin-top':'30px'
                        },
                        width=5,
                    ),
                    dbc.Col(
                        '', 
                        width=6,
                    ),
                ],
                style={
                    'color': '#0D1A51',
                    'font-family': 'Sans-serif',
                    'font-weight': 'bold',
                    'font-size': '20px',
                    'text-align':'left',
                    'height': '5rem',    
                },
            ),
        ],
        fluid=True,
    ),
)


search_content = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Markdown(
                                '''
                                **BLAST**
                                finds regions of similarity between biological sequences. 
                                The program compares nucleotide or protein sequences to sequence 
                                databases and calculates the statistical significance. 
                                ***version: blast 2.14.0***
                                '''
                            ),
                            html.Button(
                                children="Learn more",
                                id="blast-button1",
                                style={
                                    'borderStyle': 'groove',
                                    'borderRadius': '5px', 
                                    'color': '#4876FF', 
                                    'border-color': '#4876FF',
                                    'top': '10px',
                                },
                                n_clicks=0,
                            ),
                            dbc.Collapse(
                                dbc.Card(
                                    dbc.CardBody(
                                        "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity "
                                        "between sequences. The program compares nucleotide or protein sequences to sequence "
                                        "databases and calculates the statistical significance of matches. BLAST can "
                                        "be used to infer functional and evolutionary relationships between sequences as "
                                        "well as help identify members of gene families."
                                    ),
                                    style={"width": "600px"},
                                ),
                                id="blast-card1",
                                is_open=False,
                                dimension="width",
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Carousel(
                                items=[
                                    {
                                        "key": "1",
                                        "src": "/assets/ctadd-blast_illustration.02.svg",
                                        "header": "blastn",
                                        "caption": '"nucleotide sequence" vs "nucleotide sequence library"',
                                    },
                                    {
                                        "key": "2",
                                        "src": "/assets/ctadd-blast-06.png",
                                        "header": "blastx",
                                        "caption": '"nucleotide sequence" vs "protein sequence library"',
                                    },
                                    {
                                        "key": "3",
                                        "src": "/assets/ctadd-blast-peptide_search_illustration.04.svg",
                                        "header": "blastp: blast、psiblast、phiblast",
                                        "caption": '"protein sequence" vs "protein sequence library"',
                                    },
                                    {
                                        "key":"4",
                                        "src":"/assets/ctadd-blast-06.png",
                                        "header":"tblastn",
                                        "caption": '"protein sequence" vs "nucleotide sequence library"',
                                    },
                                    {
                                        "key":"5",
                                        "src":"/assets/ctadd-blast-peptide_search_illustration.04.svg",
                                        "header":"tblastx",
                                        "caption": '"Translation Sequences of nucleotide Sequences" vs "Translation Sequences of nucleotide Sequence Library"',
                                    }
                                ],
                                variant="dark",
                                ride="carousel",
                                interval=3000,
                                style={
                                    "opacity": 0.8,
                                    'width': '70%',
                                    'margin-left': '3.5rem'
                                },
                            )
                        ],
                        width=5,
                    ),
                    dbc.Col(
                        [
                            html.P(
                                'Select algorithm type:',
                                style={
                                    'color':'#5B5B5B',
                                    "backgroundColor": "#B9D3EE",
                                }
                            ),
                            dcc.Dropdown(
                                [
                                    "blastn",
                                    "blastx",
                                    "blastp",
                                    "psiblast",
                                    "phiblast",
                                    "tblastn",
                                    "tblastx",
                                ],
                                value='psiblast',
                                id="blast_type",
                                clearable=False,
                            ),
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            du.Upload(
                                id='blast_upload',
                                text='Upload Sequence File ', 
                                text_completed='Upload Success ',
                                cancel_button=True, #取消上传
                                pause_button=True, #暂停上传
                                default_style={
                                    'background-color': '#fafafa',
                                    'font-weight': 'bold',
                                    'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '60px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin-right': '10px',
                                },
                            ),
                            html.Br(),
                            dbc.Spinner(
                                html.Div(id = "output1"),
                                color="primary"
                                children=[]
                            ),
                            html.Button(
                                children="Download", 
                                id="blast_output",
                                style={
                                    'borderStyle': 'groove',
                                    'borderRadius': '5px', 
                                    'color':'#4876FF', 
                                    'border-color': '#4876FF'
                                }
                            ),
                            dcc.Download(
                                id="blast_download",
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Toast(
                                [
                                    dcc.Markdown(
                                        '''
                                            1. The upload sequence file must be commom text in Fasta format.  
                                            An example of a protein sequence file as below:  
                                            `>AP_1`  
                                            `AIGSILGALAKGLPTLISWIKNR`
                                            2. The file need only one sequence. 
                                        '''
                                    )
                                ],
                                header="Tips",
                                style={
                                    'background-color':'#EEC900',
                                    'width':'100%'
                                }
                                
                            )   
                        ],
                        width=4
                    ),
                    dbc.Col(
                        [
                            html.Br(),
                            dbc.Button(
                                id="blast_button",
                                children="Blast",
                                color="primary",
                                className="ml-2"
                            ),
                        ],
                        width=1
                    ),
                ]
            ),
        ],
        fluid=True,
    )
)


blast_page = html.Div([title_top_search, search_content])


if __name__ == '__main__':
    import sys
    sys.path.append(r'/gctadd-tool/')
    from server import app

    app.layout = blast_page
    app.run_server(debug=True)
