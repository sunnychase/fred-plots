# Economic Indicators Visualization Script

This script retrieves and visualizes economic indicators using the FRED API. You can customize it further based on your specific needs or preferences.

## Overview

This Python script retrieves and visualizes key economic indicators from the Federal Reserve Economic Data (FRED) API. The indicators include:

- M2 Money Supply
- Consumer Price Index (CPI) for inflation
- Unemployment Rate
- Overnight Reverse Repo
- Daily Reserves
- Treasury General Account (TGA)

The script generates plots for each indicator, displaying historical data and the latest values.

## Requirements

To run this script, you need the following Python packages:

- `pandas`
- `matplotlib`
- `fredapi`

You can install these packages using pip:

```bash
pip install pandas matplotlib fredapi
```

## Setup

1. **FRED API Key**: You need to obtain an API key from the FRED website. Replace the placeholder in the script with your actual API key:

   ```python
   api_key = 'your_api_key'  # Replace with your actual FRED API key
   ```

2. **Run the Script**: Execute the script in your Python environment. The script will retrieve the latest data for the specified economic indicators and generate plots.

## Functionality

- **Data Retrieval**: The script uses the `fredapi` library to fetch data for various economic indicators.
- **Data Visualization**: Each indicator is plotted using `matplotlib`, with the latest value annotated on the plot.
- **Legend Positioning**: Legends are positioned on the left side of each plot for better visibility.
- **Maximized Plots**: Each plot window is maximized for an enhanced viewing experience.

## Code Structure

- **Imports**: The necessary libraries are imported at the beginning of the script.
- **API Key Setup**: The FRED API key is initialized.
- **Data Retrieval and Plotting**: The script retrieves data for each economic indicator and generates corresponding plots.

## Example Usage

To run the script, simply execute it in your Python environment:

```bash
python economic_indicators_visualization.py
```

## Output

The script will display plots for each economic indicator, showing historical trends and the latest values. Each plot will be maximized and will have the legend positioned on the left side.

## Error Handling

The script includes basic error handling to manage issues that may arise during data retrieval. If an error occurs, a message will be printed to the console.

## License

Sunny Chase, All Rights Reserved 2025

## Acknowledgments

- [FRED API](https://fred.stlouisfed.org/) for providing access to economic data.
- [Matplotlib](https://matplotlib.org/) for data visualization.
