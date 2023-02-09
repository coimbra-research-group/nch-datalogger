"""Placeholder for plot.py script to generate html for plotly figures."""

import os
import plotly.express as px


def plot_example():
    fig = px.scatter(x=range(10), y=range(10))
    filename = os.path.join("html_plots", "pxplot_example.html")
    fig.write_html(filename)
    return None


if __name__ == "__main__":
    plot_example()
