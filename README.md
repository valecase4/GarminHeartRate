# Heart Rate Analytics with Garmin

## Description:
This project leverages heart rate data collected from the Garmin Venu SQ2 to create a comprehensive data pipeline and interactive dashboard. From raw data collection to cleaning and visualization, the goal is to uncover actionable fitness insights through Python, Jupyter, and Plotly Dash.

## Technologies Used:
- __Garmin Connect API__ (Data Collection)
- __Python__ (Data Processing, automation)


## script.py Overview: Heart Rate Data Collection

The Python script serves as the backbone of the project, automating the collection of heart rate data from the Garmin Connect platform and organizing it into structured CSV files for further analysis. By leveraging the Garmin Connect API, the script ensures seamless and efficient data retrieval for any specified date range.

### How it works:

1. __Environment Setup for Secure Authentication__: The script utilizes the dotenv library to load sensitive credentials (email and password) from a .env file. This ensures secure and environment-independent authentication with Garmin Connect.
2. __Dynamic Data Range Configuration__: The script defines a customizable date range (starting from December 21, 2024, to the current date) and automatically iterates over each day in the range to fetch daily heart rate data.
3. __Data Retrieval via Garmin Connect API__: For each date, the script connects to Garmin's servers using the Garmin library and retrieves detailed heart rate data, including timestamps and recorded heart rates.
4. __Data Organization in CSV Format__: The retrieved data is processed and saved as individual CSV files (one for each date).
Each file is stored in the data/raw/ directory and contains two key columns: 
    - timestamp: The time of each heart rate reading (in hours and minutes).
    - heart_rates: The corresponding heart rate value
