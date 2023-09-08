from dash import html, dcc,Input, Output
import dash_bootstrap_components as dbc
import dash_uploader as du

title_top = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Img(
                                src='/assets/ctadd-help-mapping-1.svg', 
                                className='img-style2'
                            ),
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4(
                                'FAQ',
                                style={
                                    'color': '#0D1A51',
                                    'font-family': 'Sans-serif',
                                    'font-weight': 'bold',
                                },
                            ),
                            
                        ],
                        width=10,
                    ),
                ],
                
                align='left',
            ),
        ],
        fluid=True,
    ),
)
help_page_content = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    html.Br(),
                    html.H5(
                        "1. How to use the blast tool to generate pssm matrices?", 
                        style={
                            'text-align':'left',
                            'color':'#0D1A51',
                        }
                    ),
                    dcc.Markdown(
                                ''' 
                                &ensp; Users can jump to the "Blast" function page in the following two ways:  
                                &emsp; (1) Click the "BLAST" option in the navigation bar. like below:  
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-blast-1.png', 
                        className='img-style12'
                    ),
                    dcc.Markdown(
                                ''' 
                                &emsp; (2) Click the "Go to blast" button on the "Home" page's below card. like below:  
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-blast-2.png', 
                        className='img-style12'
                    ),
                    dcc.Markdown(
                                ''' 
                                &ensp; Then User can select algorithm type as "psiblast" , 
                                and upload the protein sequence file ,
                                click the "Blast" button to start blast analysis.   
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-blast-3.png', 
                        className='img-style12'
                    ),
                    dcc.Markdown(
                                ''' 
                                &ensp; When the blast is completed, click the "Download"
                                button to download the result file.
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-blast-4.png', 
                        className='img-style12'
                    ),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H5(
                        "2. How to use the predict model to predict ACP/AMP?", 
                        style={
                            'text-align':'left',
                            'color':'#0D1A51',
                        }
                    ),
                    dcc.Markdown(
                                ''' 
                                &ensp; On the "Predict ACP/AMP" function page, after select predict type
                                , you can upload the sequence file only, you can also select upload the sequence
                                and the PSSM file both. Then click the "Predict" button to start predict analysis.
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-predict-1.png', 
                        className='img-style12'
                    ),
                    dcc.Markdown(
                                ''' 
                                &ensp; When the blast is completed, you can preview analysis results
                                 at the bottom of the page, click the "Export" button on the top left 
                                 of the data table to download the predict result file. 
                                '''
                    ),
                    html.Img(
                        src='/assets/help-usage-predict-2.png', 
                        className='img-style12'
                    ),
                ],
            ),
            dbc.Row(
                [
                    html.H5(),
                    html.P(),
                ]
            )
        ],
        fluid=True,
    )
)

help_page = html.Div([title_top, help_page_content])

if __name__ == '__main__':
    import sys
    sys.path.append(r'/gctadd-tool/')
    from server import app

    app.layout = help_page
    app.run_server(debug=True)
