import streamlit as st
import pandas as pd
import plotly.express as px


def scatterplot(df):

    # Create a scatter plot of GDP per capita and Life Expectancy (IHME)
    # with hover, log, size, color, title, labels
    fig = px.scatter(
        df,
        x="GDP per capita",
        y="Life Expectancy (IHME)",
        hover_name="country",
        log_x=True,
        size="GDP",
        color="country",
        title="GDP per capita vs Life Expectancy (IHME)",
        labels={
            "GDP per capita": "GDP per capita (log scale)",
            "Life Expectancy (IHME)": "Life Expectancy (IHME)",
        },
    )
    return fig
