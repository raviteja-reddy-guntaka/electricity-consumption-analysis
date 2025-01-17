from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = load_dataset("tulipa762/electricity_load_diagrams", "uci")

# Convert to pandas DataFrame
df = pd.DataFrame(dataset['train'])

# Convert 'datetime' to datetime type and set as index
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

print(df.info())
print("\nSample data:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())
