# -*- coding: utf-8 -*-
"""Portfolio Optimization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I1UPReVOY-NB3kZWWED2YAIcD9rn0yFX
"""

!pip install yfinance==0.2.40
!pip install vega_datasets

import yfinance as yf
print(yf.__version__)  # Should print 0.2.40

from pandas_datareader import data as pdr
yf.pdr_override()
pdr.get_data_yahoo(["MSFT"]).keys()

data = yf.download("AAPL MCD DIS F", interval="1mo", start="2018-12-01", end="2023-12-31")
data=data.dropna()
data.to_csv("data.csv")
import os
print(os.getcwd())

!pip install pandas

import pandas as pd

file_path = "data.csv"
data = pd.read_csv(file_path)

data = pd.read_csv("data.csv", nrows=100)

import pandas as pd

# Replace 'data.csv' with the correct file path
file_path = "data.csv"

try:
    # Load the CSV file
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")

    # Display all rows by adjusting Pandas display settings
    pd.set_option('display.max_rows', None)
    display(data)

    # Check if 'Adj Close' column exists
    if 'Adj Close' in data.columns:
        adj_close = data['Adj Close']
        print("Adj Close column extracted:")
        print(adj_close)
    else:
        print("The 'Adj Close' column does not exist in the data.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except pd.errors.EmptyDataError:
    print("The file is empty!")
except Exception as e:
    print(f"An error occurred: {e}")

import pandas as pd
from IPython.display import display, HTML

# Replace 'data.csv' with the correct file path
file_path = "data.csv"

try:
    # Load the CSV file
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")

    # Display the DataFrame in a scrollable table (if too large)
    html_table = data.to_html(max_rows=20)  # Adjust max_rows as needed
    scrollable_html = f"""
    <div style="height: 400px; overflow-y: scroll; border: 1px solid black; padding: 10px;">
        {html_table}
    </div>
    """
    display(HTML(scrollable_html))

except FileNotFoundError:
    print(f"File not found: {file_path}")
except pd.errors.EmptyDataError:
    print("The file is empty!")
except Exception as e:
    print(f"An error occurred: {e}")

import pandas as pd
# Load the Excel file to see its structure
file_path = 'Portfolio_Optimization.xlsx'
excel_data = pd.ExcelFile(file_path)
# Display the sheet names to understand the content
excel_data.sheet_names

import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with the actual file name)
df = pd.read_csv("data.csv")

# Specify the columns to focus on
columns_to_focus = ['Adj Close', 'Adj Close.1', 'Adj Close.2', 'Adj Close.3']

# Filter the DataFrame to include only the specified columns and exclude rows 0 and 1
df_filtered = df[columns_to_focus].iloc[2:]

# Perform observations
# 1. Summary statistics
print("Summary Statistics:")
print(df_filtered.describe())

# 2. View the first few rows
print("\nFirst Few Rows:")
print(df_filtered.head())

# 3. Check for missing values
print("\nMissing Values:")
print(df_filtered.isnull().sum())

# 4. Optional: Display the shape of the filtered dataset
print("\nShape of Filtered Dataset:")
print(df_filtered.shape)

# Adjust display settings to show all columns
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)       # Set a wider display width

# Assign the tickers as column headers
tickers = ['AAPL', 'DIS', 'F', 'MCD']
df_filtered.columns = tickers

# Exclude the first two rows and reset the dataset
df_filtered_60_no_header = df_filtered.iloc[0:62]  # Select rows with valid data

# Display the updated filtered dataset
print(df_filtered_60_no_header)

# Exclude rows containing ticker symbols (e.g., rows with non-numeric data)
df_filtered_60_no_header = df_filtered.iloc[1:62]  # Select rows with valid data (numerical only)

# Convert all data to numeric, coercing non-numeric data to NaN, then drop NaN rows (if needed)
df_filtered_60_no_header = df_filtered_60_no_header.apply(pd.to_numeric, errors='coerce')

# Perform observations
print("Summary Statistics:")
print(df_filtered_60_no_header.describe())

print("\nFirst Few Rows:")
print(df_filtered_60_no_header.head())

print("\nMissing Values:")
print(df_filtered_60_no_header.isnull().sum())

print("\nShape of Filtered Dataset:")
print(df_filtered_60_no_header.shape)

# Ensure all data is numeric
df_filtered_60_no_header = df_filtered_60_no_header.apply(pd.to_numeric, errors='coerce')

# Handle missing values
df_filtered_60_no_header = df_filtered_60_no_header.dropna()  # Drop rows with NaNs

# Calculate the holding period return (HPR) for each column
holding_period_returns = df_filtered_60_no_header.pct_change()

# Drop the first row since HPR cannot be calculated for it
holding_period_returns = holding_period_returns.dropna()

# Display the HPR
print("Holding Period Returns (Percentages):")
print(holding_period_returns)

# Calculate the expected return (average) from the holding period returns
expected_returns_percentages = holding_period_returns.mean()

# Display the results
print("Expected Returns (Averages as Percentages) for Each Column:")
print(expected_returns_percentages)

# Calculate the standard deviation from the holding period returns
standard_deviation_percentages = holding_period_returns.std()

# Display the results
print("Standard Deviations (as Percentages) for Each Column:")
print(standard_deviation_percentages)

# Define the risk-free rate (in percentage form)
risk_free_rate = 0.156602035237182 / 100  # Replace with the actual rate

# Calculate the Sharpe Ratio for each column
sharpe_ratios = (expected_returns_percentages - risk_free_rate) / standard_deviation_percentages

# Display the Sharpe Ratios
print("Sharpe Ratios for Each Column:")
print(sharpe_ratios)

# Rename the columns
df_filtered_60_no_header.columns = ['AAPL', 'DIS', 'F', 'MCD']

# Display the updated DataFrame to confirm
print(df_filtered_60_no_header.head())

import numpy as np

# Define portfolio weights (25% for each stock)
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Ensure `expected_returns_percentages` is a NumPy array or convert it
expected_returns_array = expected_returns_percentages.to_numpy()

# Calculate the Portfolio Expected Return using dot product
portfolio_expected_return = np.dot(weights, expected_returns_array)

# Convert Portfolio Expected Return to percentage
portfolio_expected_return_percentage = portfolio_expected_return * 100

# Display the result as a percentage
print("Portfolio Expected Return (as %): {:.2f}%".format(portfolio_expected_return_percentage))

# Assuming df_filtered_60_no_header contains the filtered Adjusted Close prices
hpr_dataframe = df_filtered_60_no_header.pct_change().dropna()

# Calculate the covariance matrix
covariance_matrix_hpr = hpr_dataframe.cov()

# Display the covariance matrix
print("Population Variance-Covariance Matrix (W):")
print(covariance_matrix_hpr)

# Get the total number of observations
n = len(hpr_dataframe)

# Calculate Ω
omega = n / (n - 1)

# Display the result
print("Ω =", omega)

# Get the total number of observations
n = len(hpr_dataframe)

# Calculate the adjustment factor
adjustment_factor = n / (n - 1)

# Calculate the Sample Variance-Covariance Matrix
sample_covariance_matrix = covariance_matrix_hpr * adjustment_factor

# Display the result
print("Sample Variance-Covariance Matrix (Ω):")
print(sample_covariance_matrix)

import numpy as np

# Define the portfolio weights
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Calculate Portfolio Variance
portfolio_variance = np.dot(np.dot(weights.T, sample_covariance_matrix), weights)

# Display the result
print("Portfolio Variance:", portfolio_variance)

import numpy as np
# portfolio_variance = <your previous code to calculate portfolio variance>
# Calculate portfolio standard deviation
portfolio_std_dev = np.sqrt(portfolio_variance)
# Convert portfolio standard deviation to percentage
portfolio_std_dev_percentage = portfolio_std_dev * 100
# Display the result as a percentage
print("Portfolio Standard Deviation (as %): {:.2f}%".format(portfolio_std_dev_percentage))

# Define the risk-free rate as a percentage and convert to decimal
risk_free_rate = 0.156602035237182 / 100
# Calculate Portfolio Sharpe Ratio
portfolio_sharpe_ratio = (portfolio_expected_return - risk_free_rate) / portfolio_std_dev
# Display the result
print("Portfolio Sharpe Ratio:", portfolio_sharpe_ratio)

import numpy as np
import pandas as pd
from scipy.optimize import minimize  # Import the minimize function
# Ticker symbols
tickers = ["AAPL", "DIS", "F", "MCD"]
# Define the covariance matrix for holding period returns (from earlier calculation)
cov_matrix = covariance_matrix_hpr.values  # Use your covariance matrix for HPR
# Define expected returns (already in percentage format)
expected_returns = expected_returns_percentages.values  # Ensure it's a NumPy array
# Number of assets
n_assets = len(expected_returns)

# Define the risk-free rate (as a decimal)
risk_free_rate = 0.00156602035237182  # Example

# Function to calculate portfolio variance
def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

# Constraint: Weights must sum to 1
constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}

# Bounds: Weights can range between -1 and 1 (allowing short-selling)
bounds = [(-1, 1) for _ in range(n_assets)]

# Initial guess (equal weights)
initial_weights = np.array([1/n_assets] * n_assets)

# Minimize portfolio variance
result = minimize(portfolio_variance, initial_weights, args=(cov_matrix,),
                  method='SLSQP', bounds=bounds, constraints=constraints)

# Extract MVP weights
mvp_weights = result.x

# Calculate Er(MVP)
er_mvp = np.dot(mvp_weights, expected_returns)

# Calculate Std(MVP)
std_mvp = np.sqrt(portfolio_variance(mvp_weights, cov_matrix))

# Calculate Sharpe Ratio (MVP)
sharpe_ratio_mvp = (er_mvp - risk_free_rate) / std_mvp

# Display results
mvp_df = pd.DataFrame({
    "Ticker": tickers,
    "Weight (%)": mvp_weights * 100
})
print(mvp_df)
print("\nEr(MVP): {:.2f}%".format(er_mvp))
print("Std(MVP): {:.2f}%".format(std_mvp * 100))
print("Sharpe Ratio (MVP): {:.4f}".format(sharpe_ratio_mvp))

import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Ticker symbols
tickers = ["AAPL", "DIS", "F", "MCD"]

# Covariance matrix and expected returns (from earlier calculations)
cov_matrix = covariance_matrix_hpr.values  # Use the HPR covariance matrix
expected_returns = expected_returns_percentages.values  # Ensure it's a NumPy array

# Risk-free rate
risk_free_rate = 0.00156602035237182  # Example

# Function to calculate portfolio return
def portfolio_return(weights, returns):
    return np.dot(weights, returns)

# Function to calculate portfolio variance
def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

# Function to minimize the negative Sharpe Ratio
def negative_sharpe_ratio(weights, returns, cov_matrix, risk_free_rate):
    ret = portfolio_return(weights, returns)
    std = np.sqrt(portfolio_variance(weights, cov_matrix))
    return -(ret - risk_free_rate) / std  # Negative for maximization

# Constraints: weights must sum to 1
constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}

# Bounds for weights (allow short selling)
bounds_short = [(-1, 1) for _ in range(len(tickers))]

# Initial guess (equal weights)
initial_weights = np.array([1 / len(tickers)] * len(tickers))

# Optimize for P* (with short selling)
result_short = minimize(negative_sharpe_ratio, initial_weights,
                        args=(expected_returns, cov_matrix, risk_free_rate),
                        method='SLSQP', bounds=bounds_short, constraints=constraints)

# Extract weights
weights_p_star_short = result_short.x
er_p_star_short = portfolio_return(weights_p_star_short, expected_returns)
std_p_star_short = np.sqrt(portfolio_variance(weights_p_star_short, cov_matrix))
sharpe_ratio_p_star_short = (er_p_star_short - risk_free_rate) / std_p_star_short

# Bounds for weights (no short selling)
bounds_no_short = [(0, 1) for _ in range(len(tickers))]

# Optimize for P* (no short selling)
result_no_short = minimize(negative_sharpe_ratio, initial_weights,
                           args=(expected_returns, cov_matrix, risk_free_rate),
                           method='SLSQP', bounds=bounds_no_short, constraints=constraints)

# Extract weights
weights_p_star_no_short = result_no_short.x
er_p_star_no_short = portfolio_return(weights_p_star_no_short, expected_returns)
std_p_star_no_short = np.sqrt(portfolio_variance(weights_p_star_no_short, cov_matrix))
sharpe_ratio_p_star_no_short = (er_p_star_no_short - risk_free_rate) / std_p_star_no_short

# Create DataFrames for results
df_short = pd.DataFrame({
    "Ticker": tickers,
    "Weight* (%)": (weights_p_star_short * 100).round(2)
})

df_no_short = pd.DataFrame({
    "Ticker": tickers,
    "Weight* (%)": (weights_p_star_no_short * 100).round(2)
})

# Display results
print("Optimal Risky Portfolio (P*) with Short Selling Allowed:")
print(df_short)
print("\nEr(P*): {:.2f}%".format(er_p_star_short * 100))
print("Std(P*): {:.2f}%".format(std_p_star_short * 100))
print("Sharpe Ratio (P*): {:.4f}".format(sharpe_ratio_p_star_short))

print("\nOptimal Risky Portfolio (P*) with No Short Selling:")
print(df_no_short)
print("\nEr(P*): {:.2f}%".format(er_p_star_no_short * 100))
print("Std(P*): {:.2f}%".format(std_p_star_no_short * 100))
print("Sharpe Ratio (P*): {:.4f}".format(sharpe_ratio_p_star_no_short))

import pandas as pd
# Data for portfolios
mvp_data = {
    "Ticker": ["AAPL", "DIS", "F", "MCD"],
    "Weight (%)": [7.98, 5.95, -6.14, 92.20],
    "Er(MVP)": [1.25, None, None, None],
    "Std(MVP)": [5.47, None, None, None],
    "Sharpe Ratio (MVP)": [0.1990, None, None, None]
}

p_star_data = {
    "Ticker": ["AAPL", "DIS", "F", "MCD"],
    "Weight (%)": [144.56, -80.71, 11.33, 24.81],
    "Er(P*)": [4.86, None, None, None],
    "Std(P*)": [11.37, None, None, None],
    "Sharpe Ratio (P*)": [0.4134, None, None, None]
}

p_star_no_short_data = {
    "Ticker": ["AAPL", "DIS", "F", "MCD"],
    "Weight (%)": [99.78, 0.00, 0.00, 0.22],
    "Er(P*) (No Short)": [3.11, None, None, None],
    "Std(P*) (No Short)": [8.63, None, None, None],
    "Sharpe Ratio (P*) (No Short)": [0.3416, None, None, None]
}

# Create DataFrames
df_mvp = pd.DataFrame(mvp_data)
df_p_star = pd.DataFrame(p_star_data)
df_p_star_no_short = pd.DataFrame(p_star_no_short_data)

# Display portfolios cleanly
print("Minimum Variance Portfolio (MVP):")
print(df_mvp.to_string(index=False))
print("\nOptimal Risky Portfolio (P*):")
print(df_p_star.to_string(index=False))
print("\nOptimal Risky Portfolio (P*) with No Short Sale:")
print(df_p_star_no_short.to_string(index=False))

"""## **Efficient Frontier Curve (Line Chart)**"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Data: Portfolio comparison
portfolio_data = pd.DataFrame({
    "Portfolio": ["MVP", "P* (Short Allowed)", "P* (No Short)"],
    "Expected Return (%)": [1.25, 4.86, 3.11],
    "Standard Deviation (%)": [5.47, 11.37, 8.63],
    "Sharpe Ratio": [0.1990, 0.4134, 0.3416]
})

# Risk-free rate (annualized in %)
risk_free_rate = 0.15  # Example: 0.15%

# Generate the Efficient Frontier Curve
weights = np.linspace(0, 1, 100)  # Linearly spaced weights
mvp_return = 1.25  # MVP Expected Return
p_star_return = 4.86  # P* Expected Return
mvp_std = 5.47  # MVP Std Dev
p_star_std = 11.37  # P* Std Dev

# Efficient Frontier formula assuming two portfolios
efficient_returns = weights * p_star_return + (1 - weights) * mvp_return
efficient_stds = np.sqrt((weights * p_star_std) ** 2 + ((1 - weights) * mvp_std) ** 2)

# Compute Sharpe Ratios for all points on the efficient frontier
sharpe_ratios = (efficient_returns - risk_free_rate) / efficient_stds

# Find the tangency portfolio (maximum Sharpe Ratio)
max_sharpe_idx = np.argmax(sharpe_ratios)
market_portfolio_return = efficient_returns[max_sharpe_idx]
market_portfolio_std = efficient_stds[max_sharpe_idx]

# Create the Capital Market Line (CML)
cml_std = np.linspace(0, max(efficient_stds) + 5, 100)  # Extend beyond market portfolio std
cml_slope = (market_portfolio_return - risk_free_rate) / market_portfolio_std
cml_returns = risk_free_rate + cml_slope * cml_std

# Create the Risk-Return Tradeoff Curve with Efficient Frontier and Risk-Free Rate
fig = go.Figure()

# Plot the efficient frontier
fig.add_trace(go.Scatter(
    x=efficient_stds,
    y=efficient_returns,
    mode='lines',
    name="Efficient Frontier",
    line=dict(color='blue', width=2)
))

# Plot individual portfolios
fig.add_trace(go.Scatter(
    x=portfolio_data["Standard Deviation (%)"],
    y=portfolio_data["Expected Return (%)"],
    mode='markers+text',
    text=portfolio_data["Portfolio"],
    name="Portfolios",
    marker=dict(size=10, color='orange')
))

# Add the risk-free rate
fig.add_trace(go.Scatter(
    x=[0],
    y=[risk_free_rate],
    mode='markers+text',
    text=["Risk-Free Rate"],
    name="Risk-Free Rate",
    marker=dict(size=10, color='green', symbol='diamond')
))

# Add the market portfolio (tangency point)
fig.add_trace(go.Scatter(
    x=[market_portfolio_std],
    y=[market_portfolio_return],
    mode='markers+text',
    text=["Market Portfolio"],
    name="Market Portfolio",
    marker=dict(size=12, color='red', symbol='circle')
))

# Add the Capital Market Line (CML)
fig.add_trace(go.Scatter(
    x=cml_std,
    y=cml_returns,
    mode='lines',
    name="Capital Market Line (CML)",
    line=dict(color='black', dash='dash', width=2)
))

# Chart Layout
fig.update_layout(
    title="Efficient Frontier with Market Portfolio and Capital Market Line",
    xaxis_title="Standard Deviation (%) (Risk)",
    yaxis_title="Expected Return (%)",
    showlegend=True,
    legend_title="Legend"
)

# Show the interactive chart
fig.show()