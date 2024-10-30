import pandas as pd
import matplotlib.pyplot as plt

# Sample CSV Data
# date,temperature
# 2024-10-01,22
# 2024-10-02,21
# 2024-10-03,23
# 2024-10-04,19
# 2024-10-05,25
# 2024-10-06,18

# Read the CSV file containing temperature data
data = pd.read_csv('temperature_data.csv', parse_dates=['date'])

# Plotting the temperature against the date
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temperature'], marker='o', linestyle='-', color='b', label='Temperature (°C)')

# Finding the highest and lowest temperature for annotations
max_temp = data['temperature'].max()
min_temp = data['temperature'].min()
max_date = data[data['temperature'] == max_temp]['date'].values[0]
min_date = data[data['temperature'] == min_temp]['date'].values[0]

# Annotating the highest and lowest temperatures on the plot
plt.annotate(f'{max_temp}°C', xy=(max_date, max_temp), xytext=(max_date, max_temp + 1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate(f'{min_temp}°C', xy=(min_date, min_temp), xytext=(min_date, min_temp - 2),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adding titles and labels
plt.title('Daily Temperature Variations')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.legend()
plt.grid()

# Show the plot
plt.tight_layout()
plt.show()


# Tricky Aspects:
# - How will you ensure that the date format is correctly interpreted by matplotlib for the x-axis?
#   To ensure that the date format is correctly interpreted by matplotlib for the x-axis, 
#   we use the 'parse_dates' parameter in pd.read_csv() to convert date strings into datetime objects.
#
# - How would you adjust the graph if the data contains missing or NaN values?
#   If the data contains missing or NaN values, we can use:
#   - data.dropna() to remove rows with NaN values, ensuring clean data for plotting.
#   - data.fillna(method='ffill') to fill NaN values with the last valid observation, 
#     allowing for continuity in the data.
