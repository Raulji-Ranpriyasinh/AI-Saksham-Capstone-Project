# Streamlit Weather Data Visualization App

This Streamlit web application allows users to upload a CSV file containing weather data, select a location, specify a date range, and visualize the data using line graphs, bar graphs, and scatter plots.

## Features

- **Upload CSV:** Users can upload a CSV file containing weather data. The CSV file must contain 'Date' and 'Location' columns.
  
- **Data Filtering:** Users can select a location and specify a date range to filter and aggregate the weather data.

- **Visualization Options:**
  - **Line Graph:** Displays trends over time for selected weather metrics.
  - **Bar Graph:** Shows comparative values across dates for selected weather metrics.
  - **Scatter Plot:** Visualizes relationships between weather metrics and dates.

## Requirements

- Python 3.7+
- Required Python packages are listed in `requirements.txt`.

## Installation

1. Clone the repository:
git clone <repository-url>
cd <repository-directory>
2. Install dependencies:
pip install -r requirements.txt
## Usage

1. Run the Streamlit app:
streamlit run app.py

2. Upload a CSV file containing weather data.

3. Select a location and specify a date range.

4. Visualize the filtered data using the provided options (Line Graph, Bar Graph, Scatter Plot).

## Example CSV File Format

Ensure your CSV file follows this format:

Date,Location,Temperature,Humidity,Wind_Speed
2024-01-01,New York,32,75,10
2024-01-02,New York,30,78,12

## Notes

- The application supports date ranges of up to 7 days due to visualization constraints.
- Ensure your CSV file has consistent date formats and numeric values for weather metrics.
