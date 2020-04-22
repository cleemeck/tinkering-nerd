# graphing templates for plotly charts
import plotly.graph_objects as go

tn_superhero_template = dict(
    layout=go.Layout(
        margin=dict(t=0, b=0, l=0, r=0),
        font_color='white',
        plot_bgcolor='#4E5D6C',
        paper_bgcolor='#4E5D6C',
        xaxis=dict(
            color='white',
            linecolor='white',
            showgrid=False,
            zeroline=False,
            automargin=True
        ),
        yaxis=dict(
            color='white',
            linecolor='white',
            showgrid=False,
            zeroline=False,
            automargin=True
        ),
        legend=dict(
            x=0.7
        ),
        geo=dict(
            projection=dict(type='natural earth'),
            landcolor='#4E5D6C',
            showocean=True,
            oceancolor='#4E5D6C',
            showcountries=True,
            countrycolor='#868e96',
            coastlinecolor='#868e96',
            showlakes=False,
            showrivers=False,
            showframe=False,
            framewidth=0,
            bgcolor='#4E5D6C'
        ),
        hoverlabel=dict(
            bgcolor='#5bc0de',
            bordercolor='#5bc0de',
            font=dict(
                color='white'
            )
        )
    )
)