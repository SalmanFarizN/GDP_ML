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


def mapplot(df):
    # Create a map plot to show as scatter plots located on each country
    # the corresponding GDP (size of the dots) and life-expectancy (colour gradient)
    fig = px.scatter_geo(
        df,
        locations="country",
        locationmode="country names",
        size="GDP",
        color="Life Expectancy (IHME)",
        hover_name="country",
        title="GDP and Life Expectancy by Country",
        projection="equirectangular",
        color_continuous_scale="Turbo",  # Modern color scale
        size_max=40,  # Larger max size for better visibility
    )
    fig.update_traces(marker=dict(line=dict(width=1, color="white"), opacity=0.8))
    fig.update_geos(
        showland=True,
        landcolor="#664423",
        showocean=True,
        oceancolor="#2b6e8e",
        showlakes=True,
        lakecolor="#467e9b",
        showcoastlines=True,
        coastlinecolor="gray",
    )
    fig.update_layout(
        title_font=dict(size=22, family="Arial", color="#333"),
        geo_bgcolor="#f9f9f9",
        margin=dict(l=0, r=0, t=60, b=0),
        coloraxis_colorbar=dict(
            title="Life Expectancy", thickness=15, len=0.5, bgcolor="#f9f9f9"
        ),
    )
    return fig
