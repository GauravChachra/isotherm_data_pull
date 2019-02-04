import pandas as pd

df = pd.read_csv('all_isotherms.csv')
print(df.head().columns)
print(df['Filename'].nunique())