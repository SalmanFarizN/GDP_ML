import streamlit as st
import pandas as pd
from src.plots import life_expectancy_vs_year, gdp_vs_year


def tab2_show(tab2, df):
    with tab2:
        # Dropdown menu to select countries
        countries = df["country"].unique()

        selected_countries = st.multiselect(
            "Select countries:", countries, key="country_multiselect_tab2"
        )

        if selected_countries:
            df_filtered = df[df["country"].isin(selected_countries)]
            fig = life_expectancy_vs_year(df_filtered)
            fig_2 = gdp_vs_year(df_filtered)

            # Create two columns for side-by-side plots
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                st.plotly_chart(fig_2, use_container_width=True)
