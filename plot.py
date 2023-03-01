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

def create_plots(df, duration):
    if duration == 'last_24_hours':
        last_ts = df['TIMESTAMP'].iloc[-1]
        start_ts = last_ts - pd.DateOffset(hours=24)
        df_plot = df[(df['TIMESTAMP'] >= start_ts) & (df['TIMESTAMP'] <= last_ts)]
        extension = '_24hrs'
    elif duration == 'last_7_days':
        date_lst = df['date'].unique()[:-7]
        df_plot = df[df['date'].isin(date_lst)]
        extension = '_7days'
    else:
        df_plot = df.copy()
        extension = ''

    fig1 = go.Figure()
    fig2 = go.Figure()
    fig3 = go.Figure()
    fig4 = go.Figure()

    fig1.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['RSR_GHI_Avg'],
        mode='markers',
        name='RSR',
        marker=dict(color='#2E86AB'))
    )

    fig1.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['PSP_GHI_Avg'],
        mode='markers',
        name='PSP',
        marker=dict(color='#659157'))
    )

    fig1.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['SPN_GHI_Avg'],
        mode='markers',
        name='SPN',
        marker=dict(color='#CB3743'))
    )

    fig2.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['RSR_DNI_Avg'],
        mode='markers',
        showlegend=True,
        name='RSR',
        marker=dict(size=5, color='#2E86AB'))
        )
    
    fig3.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['AirTemp_Avg'],
        mode='markers',
        showlegend=True,
        name='Air Temp',
        marker=dict(size=5, color='#2E86AB'))
        )

    fig4.add_trace(go.Scatter(
        x=df_plot['TIMESTAMP'],
        y=df_plot['RH_Avg'],
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

    filename1 = os.path.join("html_plots", f"ghi_plot{extension}.html")
    filename2 = os.path.join("html_plots", f"dni_plot{extension}.html")
    filename3 = os.path.join("html_plots", f"airtemp_plot{extension}.html")
    filename4 = os.path.join("html_plots", f"rh_plot{extension}.html")
    fig1.write_html(filename1)
    fig2.write_html(filename2)
    fig3.write_html(filename3)
    fig4.write_html(filename4)


if __name__ == "__main__":
    data = os.path.join("data", "NCH_01.csv")
    df = process_csv(data)
    create_plots(df, 'last_24_hours')
    create_plots(df, 'last_7_days')
    create_plots(df, 'all')
