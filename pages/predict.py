from dash import html, dcc,Input, Output
import dash_bootstrap_components as dbc
import dash_uploader as du
from callbacks.allrun import project_initial
from pages.subs.db_tools import generate_datatable,generate_table


result_content = html.Div(
    [
        dbc.Row(
            dbc.Alert(
                [
                    html.I(className="bi bi-check-circle-fill me-2"),
                    "ACP/AMP predict has completed !",
                ],
                color="success",
                className="d-flex align-items-center",
            ),
        ),
        html.Br(),
    ]
)


content = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Br(),
                            html.Br(),
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                            src="/assets/ctadd-predict-1.png",
                                            top=True,
                                            style={"opacity": 0.9},
                                    ),
                                    dbc.CardImgOverlay(
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Predict ACP/AMP", 
                                                    className="card-title",
                                                    style={'text-align':'center'}
                                                ),
                                                dcc.Markdown(
                                                    ''' 
                                                    &emsp; In recent years, AMPs, including ACPs, have
                                                    been widely used for clinical applications in a variety of disease
                                                    therapies. Accordingly, the effective identification of peptides 
                                                    with biological activity is crucial for developing candidate drugs.  
                                                    &emsp; Various experimental and computational methods have been developed. 
                                                    Traditional wet experiments are often expensive and time consuming; 
                                                    hence, the development of reliable computational methods is urgently needed. 
                                                    With the development of artificial intelligence, an increasing number of 
                                                    computational methods based on machine learning have been proposed.  
                                                    &emsp; **TriNet**
                                                    , a tri-fusion neural network for ACP and AMP prediction.  The proposed framework 
                                                    achieved substantially improved performance over that of other ACP/AMP prediction 
                                                    tools.  


                                                    &emsp; _ACP: anticancer peptides;_    
                                                    &emsp; _AMP: antimicrobial peptides._
                                                    '''
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        width=5,
                    ),
                    dbc.Col(
                        [
                            html.Br(),
                            html.Br(),
                            html.Label(
                                'Select predict type:',
                                style={
                                    "backgroundColor": "#B9D3EE",
                                    'color':'#5B5B5B',
                                    "textAlign": "center",
                                }
                            ),
                            dcc.RadioItems(
                                ['ACP','AMP', 'ALL'], 
                                'ACP',
                                id='radioItem2',
                                style={
                                    'width': 80
                                }
                            ),
                            dbc.Toast(
                                [
                                    dcc.Markdown(
                                        '''
                                            1. The upload sequence file must be commom text in Fasta format.  
                                            An example of a protein sequence file as below:  
                                            `>AP_1`  
                                            `AIGSILGALAKGLPTLISWIKNR`  
                                            The sequence id must be end with number.

                                            2. The upload PSSM file is not necessary.  
                                            When only input the fasta file run fails, it is necessary to upload the PSSM file at the same time.  
                                            The PSSM file must be named as "1.txt 2.txt ..."
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
                        width=2,
                    ),
                    dbc.Col(
                        [
                            html.Br(),
                            html.Br(),
                            html.Label(
                                "Upload the sequence file:",
                                style={
                                    'color':'#5B5B5B',
                                    "backgroundColor": "#B9D3EE",
                                }
                            ),
                            html.Br(),
                            du.Upload(
                                id='predict_upload1',
                                text='Upload File', 
                                text_completed='Upload Success ',
                                cancel_button=True, #取消上传
                                pause_button=True, #暂停上传
                                default_style={
                                    'background-color': '#fafafa',
                                    'font-weight': 'bold',
                                    'height': '30px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin-right': '1px'
                                },
                            ),
                            html.Br(),
                            html.Br(),
                            html.Label(
                                "Upload the PSSM file:",
                                style={
                                    'color':'#5B5B5B',
                                    "backgroundColor": "#B9D3EE",
                                }
                            ),
                            html.Br(),
                            du.Upload(
                                id='predict_upload2',
                                text='Upload File', 
                                text_completed='Upload Success ',
                                cancel_button=True, #取消上传
                                pause_button=True, #暂停上传
                                default_style={
                                    'background-color': '#fafafa',
                                    'font-weight': 'bold',
                                    'height': '30px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin-right': '1px'
                                },
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dbc.Button(
                                                id="example_button",
                                                children="Example",
                                                color="danger",
                                                className="ml-2"
                                            ),
                                        ],
                                        sm=6,
                                    ),
                                    dbc.Col(
                                        [

                                        ],sm=3,
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Button(
                                                id="predict_button2",
                                                children="Predict",
                                                color="primary",
                                                style={
                                                    'textAlign':'right',
                                                }
                                            ),
                                        ],
                                        sm=3,
                                        align="right",
                                    ),
                                ],
                            ),
                            html.Br(),
                            dbc.Spinner(
                                html.Div(id = "output2"),
                                color="primary"
                                children=[]
                            ),
                            dbc.Spinner(
                                html.Div(id = "output3"),
                                color="primary"
                                children=[]
                            ),
                                
                        ],
                        width=4,
                    ),
                ],
            ),
        ],
        fluid=True,
    ),
)

predict_page = html.Div([content])

if __name__ == '__main__':
    import sys
    sys.path.append(r'/gctadd-tool/')
    from server import app

    app.layout = predict_page
    app.run_server(debug=True)
