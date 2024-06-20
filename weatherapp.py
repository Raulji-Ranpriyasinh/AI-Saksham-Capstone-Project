import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to filter and aggregate data between given dates and location
def filter_and_aggregate_data(df, start_date, end_date, location):
    df['Date'] = pd.to_datetime(df['Date']).dt.date  # Extract only the date part
    mask = (df['Date'] >= pd.Timestamp(start_date).date()) & (df['Date'] <= pd.Timestamp(end_date).date()) & (df['Location'] == location)
    filtered_df = df.loc[mask]
    # Ensure only numeric columns are included in the aggregation
    numeric_columns = filtered_df.select_dtypes(include=['number']).columns
    aggregated_df = filtered_df.groupby('Date')[numeric_columns].mean().reset_index()
    return aggregated_df

# Function to plot line graph
def plot_line_graph(df):
    fig, ax = plt.subplots()
    for column in df.columns[1:]:  # Skip the 'Date' column
        ax.plot(df['Date'], df[column], marker='o', label=column)
    ax.set_title('Line Graph')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_ylim(0, 100)  # Set y-axis limit from 0 to 100
    ax.set_yticks(range(0, 101, 10))  # Set y-axis ticks every 10 units
    plt.xticks(rotation=45)
    ax.legend()
    plt.tight_layout()
    return fig

# Function to plot bar graph
def plot_bar_graph(df):
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Date', ax=ax)
    ax.set_title('Bar Graph')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_ylim(0, 100)  # Set y-axis limit from 0 to 100
    ax.set_yticks(range(0, 101, 10))  # Set y-axis ticks every 10 units
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# Function to plot scatter plot
def plot_scatter_plot(df):
    fig, ax = plt.subplots()
    for column in df.columns[1:]:  # Assuming 'Date' is the first column
        ax.scatter(df['Date'], df[column], label=column)
    ax.set_title('Scatter Plot')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_ylim(0, 100)  # Set y-axis limit from 0 to 100
    ax.set_yticks(range(0, 101, 10))  # Set y-axis ticks every 10 units
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# Streamlit app
st.title("Streamlit Weather Data Visualization App Using CSV File")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if 'Date' not in df.columns or 'Location' not in df.columns:
        st.error("CSV file must contain 'Date' and 'Location' columns.")
    else:
        df['Date'] = pd.to_datetime(df['Date'])
        
        st.write("### Uploaded Data")
        st.write(df)
        
        # Get unique locations from the data
        locations = df['Location'].unique()
        location = st.selectbox("Select Location", locations)
        
        start_date = st.date_input("Start date", df['Date'].min().date())
        end_date = st.date_input("End date", df['Date'].max().date())
        
        # Convert date_input dates to datetime.date for comparison
        start_date = pd.Timestamp(start_date).date()
        end_date = pd.Timestamp(end_date).date()
        
        if start_date > end_date:
            st.error("Error: End date must fall after start date.")
        elif (end_date - start_date).days > 7:
            st.error("Error: The date range cannot exceed 7 days.")
        else:
            filtered_df = filter_and_aggregate_data(df, start_date, end_date, location)
            
            st.write(f"### Data from {start_date} to {end_date} for {location}")
            st.write(filtered_df)
            
            st.write("## Line Graph")
            fig_line = plot_line_graph(filtered_df)
            st.pyplot(fig_line)
            
            st.write("## Bar Graph")
            fig_bar = plot_bar_graph(filtered_df)
            st.pyplot(fig_bar)
            
            st.write("## Scatter Plot")
            fig_scatter = plot_scatter_plot(filtered_df)
            st.pyplot(fig_scatter)
