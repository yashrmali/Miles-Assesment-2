# Miles-Assesment-2
# 🌡️ Daily Temperature Variations Plotter

## Overview
This project visualizes daily temperature variations using data stored in a CSV file. The script reads temperature data, processes it, and generates a line plot, highlighting the highest and lowest temperatures.

## 📊 Sample CSV Data
The expected format for the temperature data is as follows:
```
date,temperature
2024-10-01,22
2024-10-02,21
2024-10-03,23
2024-10-04,19
2024-10-05,25
2024-10-06,18
```

## 🛠️ Requirements
To run this script, you will need:
- Python 3.x
- `pandas` library
- `matplotlib` library

### Install Required Libraries
You can install the necessary libraries using pip:
```bash
pip install pandas matplotlib
```

## 🔍 Key Considerations

### Date Handling
To ensure that the date format is correctly interpreted by Matplotlib for the x-axis, we use the `parse_dates` parameter in `pd.read_csv()` to convert date strings into datetime objects.

### Handling Missing Values
If the data contains missing or NaN values, you can manage it using the following methods:
- **Remove NaN Values**: `data.dropna()` removes any rows with NaN values.
- **Fill NaN Values**: `data.fillna(method='ffill')` fills NaN values with the last valid observation, maintaining continuity in the data.

## 🚀 Getting Started
1. Create a CSV file named `temperature_data.csv` with the sample data or your own temperature data.
2. Run the script in your Python environment to visualize the temperature variations.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to modify the script to fit your data needs or improve visual aesthetics! Happy plotting! 🎉
