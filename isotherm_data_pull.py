import pandas as pd
import os

all_files = os.listdir('.\\input\\')

adsorbate_dict = {'C2H4': 'Ethylene', 'ethylene': 'Ethylene', 'Ethylene': 'Ethylene',
                  'CO2': 'Carbon Dioxide', 'carbon dioxide': 'Carbon Dioxide', 'Carbon Dioxide': 'Carbon Dioxide',
                  'C2H6': 'Ethane', 'ethane': 'Ethane', 'Ethane': 'Ethane',
                  'N2': 'Nitrogen', 'nitrogen': 'Nitrogen', 'Nitrogen': 'Nitrogen',
                  'CH4': 'Methane', 'methane': 'Methane', 'Methane': 'Methane',
                  'CO': 'Carbon Monoxide', 'carbon monoxide': 'Carbon Monoxide', 'Carbon Monoxide': 'Carbon Monoxide',
                  'H2': 'Hydrogen', 'hydrogen': 'Hydrogen', 'Hydrogen': 'Hydrogen'}

df_all_isotherms = pd.read_csv('all_isotherms.csv')

for item in all_files:

    if df_all_isotherms['Filename'].str.contains(item.split('.')[0], regex=False).any():
        pass
    else:
        if 'Kinetics' not in item:

            # Read txt file
            df = pd.read_table('.\\input\\'+item, names=[str(i) for i in range(1, 17)], sep=',')

            # Read attributes
            sample_name = df['2'].iloc[df[df['1'] == 'Sample Name'].index.item()]
            temperature = df['2'].iloc[df[df['1'] == 'Analysis Temperature (Celsius)'].index.item()]
            adsorbate = df['2'].iloc[df[df['1'] == 'Adsorbate'].index.item()]
            analysis_date = df['2'].iloc[df[df['1'] == 'Analysis Date'].index.item()]
            print(item)

            # Read pressure and loading values
            pressure_points = df['5'].iloc[df[df['5'] == 'Pc2 (Peq)'].index.item() + 1:].reset_index(drop=True)
            loading = df['16'].iloc[df[df['16'] == 'Nexc/g'].index.item() + 1:].reset_index(drop=True)
            loading = pd.to_numeric(loading)
            pressure_points = pd.to_numeric(pressure_points)

            # Make a new dataframe
            df_output = pd.DataFrame(columns=['Sample Name', 'Temperature', 'Adsorbate', 'Analysis Date',
                                              'Pressure (bar)', 'Loading (mmol/g)', 'Filename'],
                                     index=range(0, len(pressure_points)))

            # Write pressure and loading values
            df_output['Pressure (bar)'] = pressure_points
            df_output['Loading (mmol/g)'] = loading*1000
            df_output['Sample Name'] = sample_name
            df_output['Temperature'] = temperature
            df_output['Adsorbate'] = adsorbate_dict[adsorbate]
            df_output['Filename'] = item.split('.')[0]
            df_output['Analysis Date'] = analysis_date

            # Export output file
            df_output.to_csv('.\\output\\'+item.split('.')[0]+'.csv', index=None)
