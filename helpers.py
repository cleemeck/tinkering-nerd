import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def render_project_card(card_img, card_title, card_text, card_id, button_href):
    card = dbc.Card(
        children=[
            dbc.CardImg(src=card_img),
            dbc.CardBody(
                children=[
                    html.H4(card_title, className='card-title'),
                    html.P(card_text, className='card-text'),
                    dbc.Button(
                        'Let me see that',
                        className='stretched-link',
                        color='primary',
                        href=button_href)
                ]
            )
        ],
        id=card_id,
        className='h-100'
    )
    return dbc.Col(card, md=6, lg=4, className='mb-4')


def render_col_section(section_title: str, section_id: str, cols: list):
    section_header = html.H2(section_title, className='text-center my-5')
    section_cols = dbc.Row(cols)
    section = dbc.Container(
        children=[section_header, section_cols],
        id=section_id
    )
    return section


def render_fluid_section(section_title: str, text_left:str, text_right:str, section_id: str):
    section_header = html.H2(section_title, className='text-center my-5')
    section = dbc.Container(
        children=[
            section_header,
            dbc.Row(
                children=[
                    dbc.Col(
                        html.P(text_left, className='lead my-2'),
                        lg=4,
                        className='ml-auto'
                    ),
                    dbc.Col(
                        html.P(text_right, className='lead my-2'),
                        lg=4,
                        className='mr-auto'
                    ),
                ],
                className='bg-dark py-5',
            ),
        ],
        id=section_id
    )
    return section


