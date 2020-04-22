import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import flask

from app import app, server
from apps import daily_dashboard
from helpers import render_project_card, render_col_section, render_fluid_section

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_layout = html.Div(
    children=[
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink('Projects',)),
                dbc.NavItem(dbc.NavLink('About',)),
                dbc.NavItem(dbc.NavLink('Contact',))
            ],
            fluid=True,
            dark=True,
            color='dark',
            fixed=True
        ),
        dbc.Container(
            children=[
                dbc.Row(
                    children=[
                        dbc.Col(
                            children=[
                                html.Img(src='assets/bitmoji_lg_edited.png',
                                         height='250vh'
                                         ),
                                html.H1('Tinkering Nerd', style={'font-size': '5vw'}, className='my-5'),
                                html.Hr(className='bg-primary'),
                                html.H3('Data Science Aficionado', style={'font-size': '1.5vw'}, className='my-5')
                            ],
                            className='text-center',
                            width=8
                        )
                    ],
                    justify='center',
                    className='bg-dark'
                )
            ],
            fluid=True
        ),
        render_col_section(
            section_title='Projects',
            section_id='projects-section',
            cols=[
                render_project_card(
                    card_img='/static/images/virus.png',
                    card_title='Coronavirus Analytics',
                    card_text='Simple dashboard with plotly.',
                    card_id='covid19-card',
                    button_href='apps/covid-dashboard'),
                render_project_card(
                    card_img='/static/images/medal-1.png',
                    card_title='Women of Olympic Games',
                    card_text='There was an 11-years old girl with a medal',
                    card_id='women-olympics-card',
                    button_href='apps/women-olympics'),
                render_project_card(
                    card_img='/static/images/nlp.png',
                    card_title='Natural Language Processing',
                    card_text='Some experiments with NLP',
                    card_id='nlp-card',
                    button_href='apps/nlp'),
            ]),
        render_fluid_section(
            section_title='About Me',
            text_left='I like building stuff. When I don\'t work as a data scientist in finance, '
                      'I play around with machine learning, '
                      'web development, data analytics. '
                      'I have a love/hate relationship with technology. '
                      'I mostly agree with uncle Ben Parker, you know.',
            text_right='This site is fully written in python, using plotly\'s fantastic framework dash and '
                       'facultyai\'s dash-bootstrap-components. At my daily work we use them to quickly prototype '
                       'ML / Data Analytics solutions and share them with users for usefulness validation.',
            section_id='about-section'
        )
    ]
)


def serve_layout():
    if flask.has_request_context():
        return url_bar_and_content_div
    return html.Div([
        url_bar_and_content_div,
        index_layout,
        daily_dashboard.layout
    ])


app.layout =serve_layout

# Index callbacks
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return index_layout
    elif pathname == '/apps/covid-dashboard':
        return daily_dashboard.layout
    else:
        return '404'



if __name__ == '__main__':
    app.run_server(debug=True)