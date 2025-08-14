import streamlit as st
import pandas as pd


def tab3_show(tab3, df):

    # Display the dataset in tab3
    with tab3:
        # List of all countries in the dataset
        countries = df["country"].unique()
        selected_countries = st.multiselect(
            "Select countries:",
            countries,
        )

        # Add slider to select range of years
        year_range = st.slider(
            "Select year range:",
            min_value=int(df["year"].min()),
            max_value=int(df["year"].max()),
            value=(int(df["year"].min()), int(df["year"].max())),
        )

        if selected_countries or year_range:

            # Create a dummy empty dataframe
            df_filtered = pd.DataFrame()

            # Display the dataframe with the selected countries and year ranges
            # both selected country and year range selected
            if selected_countries and year_range:
                df_filtered = df[
                    df["country"].isin(selected_countries)
                    & df["year"].between(year_range[0], year_range[1])
                ]
                st.dataframe(df_filtered)

            # only countries selected
            elif selected_countries:
                df_filtered = df[df["country"].isin(selected_countries)]
                st.dataframe(df_filtered)

            # only year range selected
            elif year_range:
                df_filtered = df[df["year"].between(year_range[0], year_range[1])]
                st.dataframe(df_filtered)

            # Display download button for filtered data
            if not df_filtered.empty:
                st.download_button(
                    label="Download filtered data",
                    data=df_filtered.to_csv(index=False),
                    file_name="filtered_data.csv",
                    mime="text/csv",
                )

        # Nothing selected
        else:
            # Display the entire dataset
            st.dataframe(df)
