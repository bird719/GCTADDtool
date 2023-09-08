from dash import html, dcc,Input, Output
import dash_bootstrap_components as dbc
import dash_uploader as du

blast_card = dbc.Card(
    [
        dbc.CardImg(
                src="/assets/ctadd-home-blast-4.png",
                top=True,
                style={"opacity": 0.7},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Blast", className="card-title"),
                    html.P(
                        "We provide the function for generating PSSM matrix files for the input peptide sequences file.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Go to blast",
                        id='link_blast',
                        size='lg',
                        href="/Blast",
                        style={
                            'background-color':'#ac93e2',
                            'color':'#FFFFFF',
                            'borderRadius': '10px',
                            'borderWidth': '0px'
                        },
                    ),
                ],
            ),
        ),
    ]
)


predict_card = dbc.Card(
    [
        dbc.CardImg(
                src="/assets/ctadd-home-predict-5.png",
                top=True,
                style={"opacity": 0.4},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Predict ACP/AMP", className="card-title"),
                    dcc.Markdown(
                        '''
                        ACP: anticancer peptides;    
                        AMP: antimicrobial peptides.
                        '''
                    ),
                    dbc.Button(
                        "Go to predict",
                        id='link_predict',
                        size='lg',
                        href="/Predict",
                        style={
                            'background-color':'#ac93e2',
                            'color':'#FFFFFF',
                            'borderRadius': '10px',
                            'borderWidth': '0px'
                        },
                    ),
                ],
            ),
        ),
    ]
)

resource_card = dbc.Card(
    [
        dbc.CardImg(
                src="/assets/ctadd-home-resources-6.png",
                top=True,
                style={"opacity": 0.5},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Resoures", className="card-title"),
                    html.P(
                        "About more reference material's informations of GCTADD. ",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Go to Resoures",
                        id='link_resoures',
                        size='lg',
                        href="/Resoures",
                        style={
                            'background-color':'#ac93e2',
                            'color':'#FFFFFF',
                            'borderRadius': '10px',
                            'borderWidth': '0px'
                        },
                    ),
                ],
            ),
        ),
    ]
)
help_card = dbc.Card(
    [
        dbc.CardImg(
                src="/assets/ctadd-home-help-7.png",
                top=True,
                style={"opacity": 0.5},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Help", className="card-title"),
                    html.P(
                        "If you need more information about how to use GCTADD, you can learn from here. ",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Go to help",
                        id='link_help',
                        size='lg',
                        href="/Help",
                        style={
                            'background-color':'#ac93e2',
                            'color':'#FFFFFF',
                            'borderRadius': '10px',
                            'borderWidth': '0px'
                        },
                    ),
                ],
            ),
        ),
    ]
)


home_content = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Br(),
                            html.H5(
                                "What are peptides?", 
                                style={
                                    'text-align': 'center',
                                    'color': '#0D1A51',
                                },
                            ),
                            html.P(
                                [
                                    'Peptides are compounds that regulate cellular biological functions ',
                                    'between large molecule proteins and small molecule drugs. ',
                                ],
                                className='content-text',
                            ),
                            html.Br(),
                            html.H5(
                                "Why peptides?", 
                                style={
                                    'text-align': 'center',
                                    'color': '#0D1A51',
                                },
                            ),
                            html.P(
                                [
                                    'Due to its main source being natural peptides or natural peptide analogues, ',
                                    'its structure is usually clear and its mechanism of action is clear. Peptide drugs, ',
                                    'due to their advantages of good targeting, low immunogenicity, good tissue permeability, ',
                                    'easy synthesis and modification, high safety, and low accumulation in tissues, ',
                                    'have shown significant therapeutic effects in anti-tumor, antibacterial, ',
                                    'chronic metabolic diseases, cardiovascular diseases, immune diseases, analgesia, and other aspects. ',
                                    'Currently, there are about 100 types of peptide drugs used in clinical practice, ',
                                    'and more than 140 types of peptide drugs are currently being developed.'
                                ],
                                className='content-text',
                            ),
                            html.Img(src='/assets/ctadd-peptide2.png', className='img-style1'),
                        ],
                        width=5,
                    ),
                    dbc.Col(
                        [
                            html.Br(),
                            html.H5(
                                'TriNet',
                                style={
                                    'text-align': 'center',
                                    'color': '#0D1A51',
                                },
                            ),
                            html.Img(src='/assets/ctadd-home-gr1_lrg-3.jpg', className='img-style1'),
                            html.P(
                                [
                                    
                                ],
                                className='content-text',
                            ),
                            dcc.Markdown(
                                '''
                                    This is the deep learning framework we use to predict the properties of peptides. 
                                    It\'s a tri-fusion neural network for the prediction of anticancer and antimicrobial peptides. 
                                    The above diagram is the Flowchart of the proposed TriNet model. 
                                    TriNet\'s more information can be found online at 
                                    [https://doi.org/10.1016/j.patter.2023.100702](https://doi.org/10.1016/j.patter.2023.100702)
                                    .
                                '''
                            ),
                            html.Br(),
                            html.Br(),
                        ]
                    ),
                    html.Br(),
                    html.Br(),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(blast_card, width=3),
                    dbc.Col(predict_card, width=3),
                    dbc.Col(resource_card,width=3),
                    dbc.Col(help_card, width=3),
                ]
            ),
            html.Br(),
            html.Br(),
        ],
        fluid=True,
    )
)

home_page = home_content

if __name__ == '__main__':
    import sys
    sys.path.append(r'/gctadd-tool/')
    from server import app

    app.layout = home_page
    app.run_server(debug=True)
