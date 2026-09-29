import pandas as pd
import numpy as np

def generate_sales_data():
    # 3 years of daily data
    dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')
    n = len(dates)
    
    # Base sales
    base_sales = 500
    
    # Trend (growing slightly over time)
    trend = np.linspace(0, 300, n)
    
    # Weekly seasonality (more sales on weekends)
    weekly_seasonality = np.array([50 if d.weekday() >= 5 else -20 for d in dates])
    
    # Yearly seasonality (more sales in summer and end of year)
    yearly_seasonality = 150 * np.sin(2 * np.pi * dates.dayofyear / 365.25)
    
    # Random noise
    noise = np.random.normal(0, 30, n)
    
    # Calculate final sales
    sales = base_sales + trend + weekly_seasonality + yearly_seasonality + noise
    sales = np.maximum(sales, 0) # No negative sales
    
    df = pd.DataFrame({
        'Date': dates,
        'Sales': np.round(sales).astype(int)
    })
    
    # Save to CSV
    df.to_csv('data/store_sales.csv', index=False)
    print("Dataset generated successfully at data/store_sales.csv")

if __name__ == "__main__":
    np.random.seed(42)
    generate_sales_data()
