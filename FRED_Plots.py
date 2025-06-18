import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# Replace 'your_api_key' with your actual FRED API key
api_key = 'Enter your FRED API here'  # Make sure to replace this with your actual API key
fred = Fred(api_key=api_key)

# Function to save latest values to CSV
def save_to_csv(data_dict, filename='economic_indicators.csv'):
    df = pd.DataFrame(data_dict)
    df.to_csv(filename, index=False)

# Initialize a dictionary to store latest values
latest_values = {}

# Pull M2 data
try:
    m2_data = fred.get_series('M2')
    m2_df = pd.DataFrame(m2_data, columns=['M2'])
    m2_df.index = pd.to_datetime(m2_df.index)
    latest_values['M2'] = m2_df['M2'].iloc[-1]
except Exception as e:
    print(f"Error retrieving M2 data: {e}")

# Plotting M2 Money Supply
plt.figure(figsize=(12, 6))
plt.plot(m2_df.index, m2_df['M2'], label='M2 Money Supply', color='blue')
plt.title('M2 Money Supply Over Time')
plt.xlabel('Date')
plt.ylabel('M2 Money Supply (in billions)')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.text(m2_df.index[-1], latest_values['M2'], f'M2: {latest_values["M2"]:.2f}', 
         fontsize=10, verticalalignment='bottom', 
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()

# Pull inflation data (CPI as an example)
series_id = 'CPIAUCNS'  # Change this to the desired series ID for inflation
try:
    inflation_data = fred.get_series(series_id)
    inflation_df = pd.DataFrame(inflation_data, columns=['CPI'])
    inflation_df.index = pd.to_datetime(inflation_df.index)
    latest_values['CPI'] = inflation_df['CPI'].iloc[-1]
except Exception as e:
    print(f"Error retrieving inflation data: {e}")

# Plotting Inflation Data
plt.figure(figsize=(12, 6))
plt.plot(inflation_df.index, inflation_df['CPI'], label='CPI Inflation', color='orange')
plt.title('CPI Inflation Over Time')
plt.xlabel('Date')
plt.ylabel('CPI (Index)')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.text(inflation_df.index[-1], latest_values['CPI'], f'CPI: {latest_values["CPI"]:.2f}', 
         fontsize=10, verticalalignment='bottom', 
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()

# Pull unemployment data (Unemployment Rate)
unemployment_series_id = 'UNRATE'  # Series ID for the unemployment rate
try:
    unemployment_data = fred.get_series(unemployment_series_id)
    unemployment_df = pd.DataFrame(unemployment_data, columns=['Unemployment Rate'])
    unemployment_df.index = pd.to_datetime(unemployment_df.index)
    latest_values['Unemployment Rate'] = unemployment_df['Unemployment Rate'].iloc[-1]
except Exception as e:
    print(f"Error retrieving unemployment data: {e}")

# Plotting Unemployment Data
plt.figure(figsize=(12, 6))
plt.plot(unemployment_df.index, unemployment_df['Unemployment Rate'], label='Unemployment Rate', color='green')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.text(unemployment_df.index[-1], latest_values['Unemployment Rate'], f'Unemployment: {latest_values["Unemployment Rate"]:.2f}%', 
         fontsize=10, verticalalignment='bottom', 
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()

# Pull Overnight Reverse Repo data
reverse_repo_series_id = 'RRPONTSYD'
try:
    reverse_repo_data = fred.get_series(reverse_repo_series_id)
    reverse_repo_df = pd.DataFrame(reverse_repo_data, columns=['Overnight Reverse Repo'])
    reverse_repo_df.index = pd.to_datetime(reverse_repo_df.index)
    latest_values['Overnight Reverse Repo'] = reverse_repo_df['Overnight Reverse Repo'].iloc[-1]
except Exception as e:
    print(f"Error retrieving Overnight Reverse Repo data: {e}")

# Plotting Overnight Reverse Repo Data
plt.figure(figsize=(12, 6))
plt.plot(reverse_repo_df.index, reverse_repo_df['Overnight Reverse Repo'], label='Overnight Reverse Repo', color='purple')
plt.title('Overnight Reverse Repo Over Time')
plt.xlabel('Date')
plt.ylabel('Amount (in billions)')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.text(reverse_repo_df.index[-1], latest_values['Overnight Reverse Repo'], f'RRP: {latest_values["Overnight Reverse Repo"]:.2f}', 
         fontsize=10, verticalalignment='bottom', 
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()

# Pull Daily Reserves data
daily_reserves_series_id = 'RESBALNS'
try:
    daily_reserves_data = fred.get_series(daily_reserves_series_id)
    daily_reserves_df = pd.DataFrame(daily_reserves_data, columns=['Daily Reserves'])
    daily_reserves_df.index = pd.to_datetime(daily_reserves_df.index)
    latest_values['Daily Reserves'] = daily_reserves_df['Daily Reserves'].iloc[-1]
except Exception as e:
    print(f"Error retrieving Daily Reserves data: {e}")

# Plotting Daily Reserves Data
plt.figure(figsize=(12, 6))
plt.plot(daily_reserves_df.index, daily_reserves_df['Daily Reserves'], label='Daily Reserves', color='red')
plt.title('Daily Reserves Over Time')
plt.xlabel('Date')
plt.ylabel('Amount (in billions)')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.text(daily_reserves_df.index[-1], latest_values['Daily Reserves'], f'Reserves: {latest_values["Daily Reserves"]:.2f}', 
         fontsize=10, verticalalignment='bottom', 
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()

