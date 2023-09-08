from dash import html, dcc,Input, Output
import dash_bootstrap_components as dbc
import dash_uploader as du

title_top = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src='/assets/ctadd-resources-tech.1.svg', 
                            className='img-style2'
                        ),
                        width=2,
                    ),
                ],
                align='left',
            ),
        ],
        fluid=True,
    ),
)
download_page_content = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    html.Br(),
                    html.H5(
                        "About Blast", 
                        style={
                            'text-align':'left',
                            'color':'#0D1A51',
                        }
                    ),
                    dcc.Markdown(
                        '''
                        **Basic Local Alignment Search Tool**  [Go to Blast Web](https://blast.ncbi.nlm.nih.gov/)  
                        [Tool Download](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/)  
                        _version 2.14.0_   
                        _update Apr 26 2023_  

                        **Swissprot** The Library of Blast Tool  
                        [Database Download](https://ftp.ncbi.nlm.nih.gov/blast/db/swissprot.tar.gz)
                        '''
                    ),
                    html.Br(),
                ]
            ),
            dbc.Row(
                [
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    html.Br(),
                    html.H5(
                        "About ACP/AMP Model", 
                        style={
                            'text-align':'left',
                            'color':'#0D1A51',
                        }
                    ),
                    dcc.Markdown(
                        '''
                        **TriNet** 
                        A tri-fusion neural network for the prediction of anticancer and antimicrobial peptides 
                        [Go to Reference Article](https://doi.org/10.1016/j.patter.2023.100702)      
                         
                        '''
                    ),
                    html.Label(
                        "Performance comparison with other existing models Comparison with ACP predictors",
                        style={
                            'text-align':'center',
                            'color':'#0D1A51',
                            'font-weight': 'bold',
                        }
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr6.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr7.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr8.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.P('Figure1. Comparison of TriNet with existing models on the ACP740 dataset using 5-fold cross-validation')
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    dbc.Col(
                        [
                            html.P('Figure2. Comparison of TriNet with existing models on the ACPmain independent dataset')
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    dbc.Col(
                        [
                            html.P('Figure3. Comparison of TriNet with existing models on the ACPalternate independent dataset')
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Label(
                        "Performance comparison with other existing models Comparison with AMP predictors",
                        style={
                            'text-align':'center',
                            'color':'#0D1A51',
                            'font-weight': 'bold',
                        }
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr9.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr10.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.Img(src='/assets/gr11.jpg', className='img-style11'),
                        ],width=4
                    ),
                    dbc.Col(
                        [
                            html.P("Figure4. Comparison of TriNet with existing models on Xiao’s independent dataset")
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    dbc.Col(
                        [
                            html.P('Figure5. Comparison of TriNet with existing models on the AMPlify dataset')
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    dbc.Col(
                        [
                            html.P('Figure6. Comparison of TriNet with existing models on the DAMP dataset')
                        ],width=4,
                        style={
                            'text-align':'center'
                        }
                    ),
                    
                ]
            ),
        ],
        fluid=True,
    )
)

resources_page = html.Div([title_top, download_page_content])

if __name__ == '__main__':
    import sys
    sys.path.append(r'/gctadd-tool/')
    from server import app

    app.layout = download_page
    app.run_server(debug=True)
