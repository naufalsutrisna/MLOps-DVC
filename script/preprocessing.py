import pandas as pd

# Load the dataset
df = pd.read_csv('data/iris.csv')

# Rename the 'species' column to 'target'
df.rename(columns={'species': 'target'}, inplace=True)

# Save the modified dataset back to iris.csv
df.to_csv('data/iris.csv', index=False)
