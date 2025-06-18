## Federal Reserve Plots

## Economic Data Visualization Script

## Overview
This Python script retrieves and visualizes key economic indicators from the Federal Reserve Economic Data (FRED) API. The indicators included in this script are:

1. M2 Money Supply
2. Consumer Price Index (CPI) Inflation
3. Unemployment Rate

The script generates line plots for each of these indicators over time, displaying the latest values directly on the graphs.

## Requirements
To run this script, you need the following Python packages:
- pandas
- matplotlib
- fredapi

You can install these packages using pip:

```pip install pandas matplotlib fredapi'''


Setup
1. API Key: You need to obtain an API key from the FRED website. Replace the placeholder in the script with your actual API key:

    api_key = 'your_api_key'  # Replace with your actual FRED API key

2. Run the Script: Execute the script in your Python environment. It will automatically fetch the data and generate the plots.

Functionality
1.  M2 Money Supply: The script retrieves the M2 money supply data and plots it over time. The latest M2 value is displayed on the plot.
2.  CPI Inflation: The script retrieves the Consumer Price Index (CPI) data and plots it over time. The latest CPI value is displayed on the plot.
3.   Unemployment Rate: The script retrieves the unemployment rate data and plots it over time. The latest unemployment rate is displayed on the plot.

Output
The script generates three separate plots:

1. M2 Money Supply Over Time
2. CPI Inflation Over Time
3. Unemployment Rate Over Time
Each plot includes a legend, grid lines, and a text box indicating the latest value of the respective indicator.

Additional Features
1. Error handling is implemented to manage issues with data retrieval.
2. You can modify the script to include additional economic indicators or customize the date range for data retrieval.
License
This script is provided for educational purposes. Feel free to modify and use it as needed.

Contact
For any questions or feedback, please contact [Your Name] at [Your Email Address].


### Instructions for Use
- Replace `[Your Name]` and `[Your Email Address]` with your actual contact information.
- Save this text in a file named `README.txt` in the same directory as your script. 

This README provides a clear overview of what the script does, how to set it up, and what output to expect, making it easier for others (or yourself in the future) to understand and use the script.
