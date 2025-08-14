# Worldwide Analysis of Quality of Life and Economic Factors

## Overview

This project provides an interactive Streamlit application to explore the relationships between poverty, life expectancy, and GDP across various countries and years. The app enables users to visualize trends, compare metrics, and analyze data through dynamic plots and tables.

The application is deployed at: [Streamlit App](https://salmanfarizn-gdp-ml-main-ke5nnw.streamlit.app)

## Data Sources

The dataset used in this project, `global_development_data.csv`, is a cleaned and merged compilation of three datasets:

1. **Poverty Data**
   - Source: [Poverty Dataset](https://raw.githubusercontent.com/owid/poverty-data/main/datasets/pip_dataset.csv)
   - Description: Provides data on poverty levels across countries.

2. **Life Expectancy Data**
   - Source: [Life Expectancy Dataset](https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Healthy%20Life%20Expectancy%20-%20IHME/Healthy%20Life%20Expectancy%20-%20IHME.csv)
   - Description: Contains data on healthy life expectancy as estimated by IHME.

3. **GDP Data**
   - Source: [GDP Dataset](https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020))/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020)).csv)
   - Description: Includes historical GDP data from the Maddison Project Database.

The merged dataset can be accessed directly at: [Global Development Data](https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv)

## Features

- **Global Overview**: Visualize worldwide trends in GDP, life expectancy, and poverty.
- **Country Deep Dive**: Analyze metrics for selected countries over time.
- **Data Explorer**: Interact with the dataset through filtering and dynamic tables.
- **Plots**:
  - Scatter plots for GDP vs Life Expectancy.
  - Geographic maps showing GDP and Life Expectancy by country.
  - Line plots for Life Expectancy and GDP trends over the years.

## Installation

To run the app locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/SalmanFarizN/GDP_ML.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GDP_ML
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

## Project Structure

- `src/`
  - `plots.py`: Contains functions to generate various plots.
  - `tab1_funcs.py`, `tab2_funcs.py`, `tab3_funcs.py`: Define the logic for different tabs in the Streamlit app.
  - `practical.py`: Main Streamlit script for the application.
- `global_development_data.csv`: Merged dataset used in the app.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Our World in Data](https://ourworldindata.org/) for providing the datasets.
- [Streamlit](https://streamlit.io/) for enabling rapid development of interactive web applications.
