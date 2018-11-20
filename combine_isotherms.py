import pandas as pd
import os

all_files = os.listdir('.\\output\\')

df_all_isotherms = pd.read_csv('all_isotherms.csv')

for item in all_files:

    if df_all_isotherms['Filename'].str.contains(item.split('.')[0], regex=False).any():
        pass
    else:
        df = pd.read_csv('.\\output\\'+item)
        df_all_isotherms = df_all_isotherms.append(df, ignore_index=True)

df_all_isotherms.to_csv('all_isotherms.csv', index=False)
