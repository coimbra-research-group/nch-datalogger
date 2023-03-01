"""Placeholder for plot.py script to generate html for plotly figures."""

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def process_csv(file):
    df = pd.read_csv(file)
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    df['date'] = df['TIMESTAMP'].dt.date.astype('str')
    df = df.sort_values(by='TIMESTAMP')
    return df

def create_plots(df):
    fig1 = go.Figure()
    fig2 = go.Figure()
    fig3 = go.Figure()
    fig4 = go.Figure()

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['RSR_GHI_Avg'],
        mode='markers',
        name='RSR',
        marker=dict(color='#2E86AB'))
    )

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['PSP_GHI_Avg'],
        mode='markers',
        name='PSP',
        marker=dict(color='#659157'))
    )

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['SPN_GHI_Avg'],
        mode='markers',
        name='SPN',
        marker=dict(color='#CB3743'))
    )

    fig2.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['RSR_DNI_Avg'],
        mode='markers',
        showlegend=True,
        name='RSR',
        marker=dict(size=5, color='#2E86AB'))
        )
    
    fig3.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['AirTemp_Avg'],
        mode='markers',
        showlegend=True,
        name='Air Temp',
        marker=dict(size=5, color='#2E86AB'))
        )

    fig4.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['RH_Avg'],
        mode='markers',
        showlegend=True,
        name='RH',
        marker=dict(size=5, color='#2E86AB'))
        )

    fig1.update_xaxes(title_text='time(local)')
    fig2.update_xaxes(title_text='time(local)')
    fig3.update_xaxes(title_text='time(local)')
    fig4.update_xaxes(title_text='time(local)')

    fig1.update_yaxes(title_text="W/m<sup>2")
    fig2.update_yaxes(title_text="W/m<sup>2")
    fig3.update_yaxes(title_text="Air Temp")
    fig4.update_yaxes(title_text="RH")

    fig1.update_traces(marker=dict(size=5))

    fig1.update_layout(
        title='GHI',
        yaxis_range=[0, 1200],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0)
    )
    fig2.update_layout(
        title='DNI',
        yaxis_range=[0, 1200],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0)
    )
    fig3.update_layout(
        title='Air Temperature',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0)
    )
    fig4.update_layout(
        title='RH',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0)
    )

    filename1 = os.path.join("html_plots", "ghi_plot.html")
    filename2 = os.path.join("html_plots", "dni_plot.html")
    filename3 = os.path.join("html_plots", "airtemp_plot.html")
    filename4 = os.path.join("html_plots", "rh_plot.html")
    fig1.write_html(filename1)
    fig2.write_html(filename2)
    fig3.write_html(filename3)
    fig4.write_html(filename4)


if __name__ == "__main__":
    data = os.path.join("data", "NCH_01.csv")
    df = process_csv(data)
    create_plots(df)
