# Time Series Model Integration Guide

## ✅ Model Status: READY FOR USE

The time series forecasting model is complete and ready to be integrated with the choice model and optimization model.

## Quick Start

### 1. Load the Model

**Note:** The model file (`time_series_model.pkl`) is not in git because it's too large. You have two options:

**Option A: Run the notebook to generate the model** (Recommended)
```python
# Run all cells in time_series.ipynb to generate the model
# The model will be saved to predictions/results/time_series_model.pkl
```

**Option B: Load saved model** (if someone shares it separately)
```python
import pickle
import pandas as pd

# Load saved model
with open('predictions/results/time_series_model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    model = model_data['model']
    last_date = model_data['last_date']
    excluded_movies = model_data['most_recent_25_movies']
```

**Option C: Use the function directly** (Easiest)
```python
# Copy the predict_total_weekly_demand() function from time_series.ipynb
# It will use the full_fitted_model variable from the notebook
```

### 2. Get Weekly Forecasts

```python
# Forecast for a specific week or range
weekly_forecast = predict_total_weekly_demand('2025-12-01', '2025-12-31')

# Output format:
# - week_start: Monday date of each week
# - predicted_demand: Total weekly gross revenue (in 2024-adjusted dollars)
# - lower_bound: Lower 95% confidence bound
# - upper_bound: Upper 95% confidence bound
```

## Integration with Choice Model

### Step-by-Step:

1. **Get weekly demand forecast**:
   ```python
   weekly_forecast = predict_total_weekly_demand('2025-12-01', '2025-12-07')
   ```

2. **Extract total demand for each week**:
   ```python
   for idx, row in weekly_forecast.iterrows():
       week_start = row['week_start']
       total_weekly_demand_dollars = row['predicted_demand']
       
       # Convert to number of customers (if choice model needs customers)
       avg_ticket_price = 11.31  # 2024 average ticket price
       total_customers = total_weekly_demand_dollars / avg_ticket_price
   ```

3. **Pass to choice model**:
   ```python
   # Use the predict_movie_demand_shares function from choice_modeling.ipynb
   demand_shares = predict_movie_demand_shares(
       total_demand_forecast=total_customers,  # or total_weekly_demand_dollars
       movies_available=available_movies
   )
   ```

### Example:

```python
# Get forecast for next week
forecast = predict_total_weekly_demand('2025-12-01', '2025-12-07')

# For each week in the forecast
for idx, row in forecast.iterrows():
    total_weekly_demand = row['predicted_demand']  # In dollars
    
    # Convert to customers
    total_customers = total_weekly_demand / 11.31
    
    # Get demand shares for each movie
    movie_demands = predict_movie_demand_shares(
        total_demand_forecast=total_customers,
        movies_available=available_movies
    )
    
    # movie_demands now contains expected demand per movie
```

## Integration with Optimization Model

### Step-by-Step:

1. **Get weekly forecasts for planning period**:
   ```python
   # Forecast for next 4 weeks (or your planning horizon)
   start_date = '2025-12-01'
   end_date = '2025-12-28'  # 4 weeks
   
   weekly_forecast = predict_total_weekly_demand(start_date, end_date)
   ```

2. **Convert to daily demand** (if optimization model needs daily):
   ```python
   # Daily demand distribution weights (weekends get more)
   daily_weights = {
       'Monday': 0.8,
       'Tuesday': 0.8,
       'Wednesday': 0.9,
       'Thursday': 1.0,
       'Friday': 1.3,
       'Saturday': 1.6,
       'Sunday': 1.6
   }
   
   # Distribute weekly demand across 7 days
   daily_demand = {}
   for idx, row in weekly_forecast.iterrows():
       week_start = row['week_start']
       weekly_total = row['predicted_demand']
       total_weight = sum(daily_weights.values())
       
       for day_offset, (day_name, weight) in enumerate(daily_weights.items()):
           date = week_start + pd.Timedelta(days=day_offset)
           daily_demand[date] = (weekly_total * weight) / total_weight
   ```

3. **Use excluded movies list**:
   ```python
   # Load the 25 most recent movies (excluded from training)
   excluded_movies = pd.read_csv('predictions/results/excluded_recent_25_movies.csv')
   
   # These movies are available for optimization
   # They were excluded from time series training to avoid data leakage
   ```

## Important Notes

### Model Characteristics:
- **Forecast Frequency**: Weekly (Monday to Monday)
- **Units**: Total weekly gross revenue in 2024-adjusted dollars
- **Excluded Data**: 
  - 25 most recent movies (reserved for optimization model)
  - COVID period (March 2020 - December 2021)
- **Model Type**: SARIMA with yearly seasonality (52 weeks)

### Output Format:
```python
# DataFrame with columns:
# - week_start: pd.Timestamp (Monday of each week)
# - predicted_demand: float (total weekly gross in dollars)
# - lower_bound: float (95% confidence lower bound)
# - upper_bound: float (95% confidence upper bound)
```

### Files Generated:
- `predictions/results/time_series_model.pkl` - Saved model
- `predictions/results/time_series_forecasts.csv` - Sample forecasts
- `predictions/results/excluded_recent_25_movies.csv` - List of excluded movies

## Common Questions

**Q: Do I need to convert dollars to customers?**  
A: It depends on what your choice model expects. The choice model in `choice_modeling.ipynb` accepts `total_demand_forecast` which can be either dollars or customers. Check the function signature.

**Q: How do I handle weekly forecasts if my model needs daily?**  
A: Use the daily distribution weights provided above to split weekly demand across 7 days.

**Q: What if I need forecasts for dates in the past?**  
A: The function will return historical data from the training set for past dates.

**Q: Can I use the model without running the notebook?**  
A: Yes! Load the saved `.pkl` file and use the `predict_total_weekly_demand()` function. You can copy the function definition to your own notebook.

## Troubleshooting

**Error: "weekly_demand_ts_no_covid is not defined"**  
→ Make sure you've run all cells in the time_series.ipynb notebook, or load the saved model from the .pkl file.

**Error: "full_fitted_model is not defined"**  
→ Either run the notebook to generate the model, or load it from the saved .pkl file.

**Forecasts seem too high/low**  
→ Remember: forecasts are in 2024-adjusted dollars. If comparing to raw historical data, account for inflation.

## Contact

If you have questions about the time series model, refer to:
- Section 13 in `time_series.ipynb` for detailed integration guide
- The function docstring in `predict_total_weekly_demand()` for parameter details

