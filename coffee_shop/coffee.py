import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook
import matplotlib.pyplot as plt

#  Create Excel Files with Dummy Data

# Coffee Seeds Data
import pandas as pd

# Original seed data
seed_data = {
    'Supplier': ['Coorg', '', 'Supplier C', 'Supplier A', 'Supplier B'],
    'Year': [2021, 2021, 2021, 2022, 2022],
    'Seeds Bought (kg)': [500, 600, 550, 520, 580],
    'Sales Generated ($)': [5000, 6200, 5800, 5300, 6000]
}

# Adding more data entries
extended_data = {
    'Supplier': ['Supplier D', 'Supplier E', 'Supplier F', 'Supplier G', 'Supplier H', 
                 'Coorg', 'Supplier C', 'Supplier B', 'Supplier A', 'Supplier D',
                 'Supplier E', 'Supplier F', 'Supplier G', 'Supplier H', 
                 'Coorg', 'Supplier C', 'Supplier B', 'Supplier A', 'Supplier D', 
                 'Supplier E', 'Supplier F'],
    'Year': [2021, 2021, 2021, 2022, 2022, 
             2022, 2022, 2021, 2021, 2022, 
             2021, 2021, 2022, 2022, 
             2022, 2021, 2022, 2022, 2021, 
             2022, 2021],
    'Seeds Bought (kg)': [550, 610, 570, 530, 590, 
                          510, 560, 580, 600, 530, 
                          590, 560, 580, 620, 
                          590, 600, 540, 570, 550, 
                          620, 540],
    'Sales Generated ($)': [5100, 6300, 6000, 5400, 6100, 
                            5100, 6000, 5500, 5800, 5400, 
                            6000, 5800, 6000, 6400, 
                            5900, 6100, 5700, 6000, 5600, 
                            6500, 5800]
}

# Combine the original data with the new extended data
full_data = seed_data.copy()
full_data.update(extended_data)

# Create a DataFrame
df = pd.DataFrame(full_data)

# Display the first few rows of the data
print(df)

# Coffee Sales Data
sales_data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Instant Coffee Sales ($)': np.random.randint(1000, 5000, 12),
    'Filter Coffee Sales ($)': np.random.randint(1500, 5500, 12)
}
sales_df = pd.DataFrame(sales_data)
sales_df.to_excel('Coffee_Sales.xlsx', index=False)

# Customer Feedback Data
feedback_data = {
    'Customer ID': range(1, 21),
    'Water Quantity Feedback': np.random.choice(['Too Much', 'Just Right', 'Too Little'], 20)
}
feedback_df = pd.DataFrame(feedback_data)
feedback_df.to_excel('Customer_Feedback.xlsx', index=False)

# Sweetener Sales Data
sweetener_data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Sugar Sales ($)': np.random.randint(1000, 3000, 12),
    'Jaggery Sales ($)': np.random.randint(800, 2500, 12),
    'Sugar-Free Sales ($)': np.random.randint(500, 2000, 12)
}
sweetener_df = pd.DataFrame(sweetener_data)
sweetener_df.to_excel('Sweetener_Sales.xlsx', index=False)

#  Analyzing the Best Coffee Seed Supplier
seeds_summary = df.groupby('Supplier').agg({'Sales Generated ($)': 'sum'}).sort_values(by='Sales Generated ($)', ascending=False)
print("Best Supplier Based on Sales:\n", seeds_summary)

#  Comparing Instant and Filter Coffee Sales
sales_df['Difference'] = sales_df['Filter Coffee Sales ($)'] - sales_df['Instant Coffee Sales ($)']
print("\nComparison of Sales:\n", sales_df[['Date', 'Difference']])

#  Customer Feedback Analysis
feedback_summary = feedback_df['Water Quantity Feedback'].value_counts()
print("\nCustomer Feedback on Water Quantity:\n", feedback_summary)

#  Comparing Coffee Sales with Different Sweeteners
sweetener_summary = sweetener_df[['Sugar Sales ($)', 'Jaggery Sales ($)', 'Sugar-Free Sales ($)']].sum()
print("\nSweetener Sales Comparison:\n", sweetener_summary)

#  Seasonal Trends Analysis
def seasonal_trends(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    monthly_sales = df.groupby('Month')[['Instant Coffee Sales ($)', 'Filter Coffee Sales ($)']].sum()

    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind='bar', edgecolor='black')
    plt.title('Seasonal Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.show()

# Calling the seasonal trends function
seasonal_trends(sales_df)


#  Customer Satisfaction Analysis
def customer_satisfaction(df):
    feedback_mapping = {'Too Much': 1, 'Too Little': 1, 'Just Right': 3}
    df['Satisfaction Score'] = df['Water Quantity Feedback'].map(feedback_mapping)

    satisfaction_summary = df['Satisfaction Score'].mean()

    plt.figure(figsize=(10, 6))
    df['Satisfaction Score'].plot(kind='hist', bins=3, edgecolor='black', color='goldenrod')
    plt.title('Customer Satisfaction Score Distribution')
    plt.xlabel('Satisfaction Score')
    plt.ylabel('Frequency')
    plt.show()

    print(f"Average Customer Satisfaction Score: {satisfaction_summary:.2f}")

# Calling the customer satisfaction function
customer_satisfaction(feedback_df)

#  Supply Chain Analysis
def supply_chain_analysis(df):
    supplier_sales = df.groupby('Supplier')['Sales Generated ($)'].sum()

    plt.figure(figsize=(10, 6))
    supplier_sales.plot(kind='bar', edgecolor='black', color='purple')
    plt.title('Supply Chain Analysis by Supplier')
    plt.xlabel('Supplier')
    plt.ylabel('Sales Generated ($)')
    plt.show()

# Calling the supply chain analysis function
supply_chain_analysis(df)

digital_presence_data = {
    'Month': pd.date_range(start='2023-01-01', periods=12, freq='M').month,
    'Website Traffic': np.random.randint(1000, 10000, 12),
    'Social Media Engagement': np.random.randint(100, 5000, 12),
    'Online Sales ($)': np.random.randint(2000, 10000, 12)
}
digital_presence_df = pd.DataFrame(digital_presence_data)
print("\nDigital Presence Analytics:\n", digital_presence_df)

# Visualize Digital Presence Data
def visualize_digital_presence(df):
    df['Month'] = df['Month'].apply(lambda x: pd.Timestamp(x, unit='M').strftime('%B'))

    plt.figure(figsize=(12, 6))
    
    # Plot Website Traffic
    plt.subplot(3, 1, 1)
    plt.plot(df['Month'], df['Website Traffic'], marker='o', linestyle='-', color='b')
    plt.title('Monthly Website Traffic')
    plt.xlabel('Month')
    plt.ylabel('Website Traffic')
    
    # Plot Social Media Engagement
    plt.subplot(3, 1, 2)
    plt.plot(df['Month'], df['Social Media Engagement'], marker='o', linestyle='-', color='g')
    plt.title('Monthly Social Media Engagement')
    plt.xlabel('Month')
    plt.ylabel('Social Media Engagement')
    
    # Plot Online Sales
    plt.subplot(3, 1, 3)
    plt.plot(df['Month'], df['Online Sales ($)'], marker='o', linestyle='-', color='r')
    plt.title('Monthly Online Sales')
    plt.xlabel('Month')
    plt.ylabel('Online Sales ($)')
    
    plt.tight_layout()
    plt.show()

# Calling the visualize digital presence function
visualize_digital_presence(digital_presence_df)