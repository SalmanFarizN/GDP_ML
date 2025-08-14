from src.tab3_funcs import tab3_show
from src.tab1_funcs import tab1_show
import streamlit as st
import pandas as pd


def main():
    # Use whole width of the page
    st.set_page_config(layout="wide")

    # Write header
    st.header("Worldwide Analysis of Quality of Life and Economic Factors")

    # Write subtitle
    st.subheader(
        "This app enables you to explore the relationships between poverty, "
        "life expectancy, and GDP across various countries and years. "
        "Use the panels to select options and interact with the data."
    )

    # Create tabs
    tab1, tab2, tab3 = st.tabs(
        ["Global Overview", "Country Deep Dive", "Data Explorer"]
    )

    # Read the dataset from data folder using pandas
    df = pd.read_csv("data/global_development_data.csv")

    with tab3:
        tab3_show(tab3, df)

    with tab1:
        tab1_show(tab1, df)


if __name__ == "__main__":
    main()
