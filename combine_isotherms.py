import pandas as pd
import os

all_files = os.listdir('.\\output\\')

df_all_isotherms = pd.read_csv('all_isotherms.csv')

# print(df_all_isotherms['filename'].str.contains('hello').any())

for item in all_files:
    # df_all_isotherms['filename'].str.contains(item.split('.')[0], regex=False).to_csv(item+'bool.csv')


    if df_all_isotherms['Filename'].str.contains(item.split('.')[0], regex=False).any() == True:
        pass
    else:
        df = pd.read_csv('.\\output\\'+item)
        df_all_isotherms = df_all_isotherms.append(df, ignore_index=True)

#     if item.split('.')[0] in df_all_isotherms['filename'] == True:
#         print('True')
#
df_all_isotherms.to_csv('all_isotherms.csv', index=False)