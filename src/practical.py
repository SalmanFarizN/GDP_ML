import streamlit as st
import pandas as pd

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
tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

# Read the dataset from data folder using pandas
df = pd.read_csv("data/global_development_data.csv")

# Display the dataset in tab3
with tab3:
    # List of all countries in the dataset
    # countries = df["country"].unique()
    # selected_countries = st.multiselect(
    #     "Select countries:",
    #     countries,
    # )

    # Display the entire dataframe
    st.dataframe(df)

    # df_filtered = df[df["country"].isin(selected_countries)]
    # st.dataframe(df_filtered)
