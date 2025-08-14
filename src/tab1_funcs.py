import streamlit as st
import pandas as pd
from src.plots import scatterplot
from src.model import model_predict
import joblib


def tab1_show(tab1, df):

    # Display the dataset in tab1
    with tab1:
        # Add a slider to select a single year
        year = st.slider(
            "Select a year:",
            min_value=int(df["year"].min()),
            max_value=int(df["year"].max()),
            value=int(df["year"].min()),
        )

        # Filter the dataframe based on the selected year
        df_filtered = df[df["year"] == year]

        # Number of unique countries
        num_unique_countries = df_filtered["country"].nunique()
        st.write(
            f"Number of Countries in the survey for {year}: {num_unique_countries}"
        )

        # Calculate the mean of Life Expectancy (IHME)
        mean_life_expectancy = df_filtered["Life Expectancy (IHME)"].mean()
        st.write(f"Mean Life Expectancy (IHME) for {year}: {mean_life_expectancy:.2f}")

        # Calculate the mean of GDP per capita
        mean_gdp_per_capita = df_filtered["GDP per capita"].mean()
        st.write(f"Mean GDP per capita for {year}: $ {mean_gdp_per_capita:.2f}")

        # Calculate the mean of headcount_ratio_upper_mid_income_povline
        mean_headcount_ratio = df_filtered[
            "headcount_ratio_upper_mid_income_povline"
        ].mean()
        st.write(
            f"Mean Headcount Ratio (Upper Middle Income Poverty Line) for {year}: {mean_headcount_ratio:.2f}"
        )

        fig = scatterplot(df_filtered)
        st.plotly_chart(fig)

        # Add fields to enter GDP per capita, headcount_ratio_upper_mid_income_povline, and year
        gdp_per_capita = st.number_input("Enter GDP per capita:", min_value=0.0)
        headcount_ratio = st.number_input(
            "Enter Headcount Ratio (Upper Middle Income Poverty Line):", min_value=0.0
        )
        year_lifepred = st.number_input(
            "Enter Year:",
            min_value=int(df["year"].min()),
            max_value=int(df["year"].max()),
        )

        # Load the model from models directory
        model = joblib.load("models/RF_gdp_model.pkl")

        # Pass the values to model_predict() to make a prediction
        if st.button("Predict Life Expectancy (IHME)"):
            if gdp_per_capita <= 0 or headcount_ratio < 0 or year_lifepred < 0:
                st.error(
                    "Please enter valid values for GDP per capita and headcount ratio."
                )
            else:
                prediction = model_predict(
                    model,
                    pd.DataFrame(
                        {
                            "GDP per capita": [gdp_per_capita],
                            "headcount_ratio_upper_mid_income_povline": [
                                headcount_ratio
                            ],
                            "year": [year_lifepred],
                        }
                    ),
                )
                st.write(
                    f"Predicted Life Expectancy (IHME) for {year_lifepred}: {prediction[0]:.2f} Years"
                )
