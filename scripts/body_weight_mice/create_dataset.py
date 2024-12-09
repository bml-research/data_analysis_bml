import pandas as pd
import numpy as np

def generate_weight_data(start_date, end_date, initial_weights, daily_gains, noise_factor=0.1):
    """Generates a DataFrame with daily weight data for multiple mouse strains.

    Args:
        start_date: Start date of the experiment.
        end_date: End date of the experiment.
        initial_weights: A list of initial weights for each strain.
        daily_gains: A list of average daily weight gains for each strain.
        noise_factor: Factor to control the magnitude of random fluctuations.

    Returns:
        A pandas DataFrame with daily weight data.
    """

    date_range = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=date_range, columns=['Wild-type', 'OB/OB', 'DB/DB'])

    # Initialize weights
    df.iloc[0] = initial_weights

    # Generate daily weights with random fluctuations
    for i in range(1, len(date_range)):
        df.iloc[i] = df.iloc[i-1] + daily_gains + np.random.randn(3) * noise_factor

    return df

# Define parameters
start_date = '2020-01-01'
end_date = '2020-12-31'
initial_weights = [20, 20, 20]  # Wild-type, OB/OB, DB/DB
daily_gains = [0.1, 0.16, 0.17]  # Daily weight gain for each strain

# Generate the dataset
df = generate_weight_data(start_date, end_date, initial_weights, daily_gains)

# Print or save the DataFrame
print(df)
#df.to_csv('mouse_weight_data.csv', index=False)
df.to_csv('mouse_weight_data.csv', index=True)