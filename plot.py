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

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['RSR_GHI_Avg'],
        mode='markers',
        name='RSR')
    )

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['PSP_GHI_Avg'],
        mode='markers',
        name='PSP')
    )

    fig1.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['SPN_GHI_Avg'],
        mode='markers',
        name='SPN')
    )

    fig2.add_trace(go.Scatter(
        x=df['TIMESTAMP'],
        y=df['RSR_DNI_Avg'],
        mode='markers',
        showlegend=True,
        name='RSR')
        )

    fig1.update_xaxes(title_text='time(local)')
    fig2.update_xaxes(title_text='time(local)')
    fig1.update_yaxes(title_text="$W/m^2$")
    fig2.update_yaxes(title_text="$W/m^2$")
    fig1.update_layout(title='GHI', yaxis_range=[0, 1200])
    fig2.update_layout(title='DNI', yaxis_range=[0, 1200])

    filename1 = os.path.join("html_plots", "ghi_plot.html")
    filename2 = os.path.join("html_plots", "dni_plot.html")
    fig1.write_html(filename1)
    fig2.write_html(filename2)


if __name__ == "__main__":
    data = os.path.join("data", "NCH_01.csv")
    df = process_csv(data)
    create_plots(df)
