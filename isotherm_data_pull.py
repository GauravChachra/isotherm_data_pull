import pandas as pd
import os

all_files = os.listdir('.\\input\\')

for item in all_files:
    print(item)

    # Read txt file
    df = pd.read_table('.\\input\\'+item, names=[str(i) for i in range(1, 17)], sep=',')

    # Read attributes
    material = df['2'].iloc[df[df['1'] == 'Sample Name'].index.item()]
    temperature = df['2'].iloc[df[df['1'] == 'Analysis Temperature (Celsius)'].index.item()]
    adsorbate = df['2'].iloc[df[df['1'] == 'Adsorbate'].index.item()]

    # Make a new dataframe
    df_output = pd.DataFrame(columns=['Experiment Attribute', 'Value', 'Pressure (bar)', 'Loading (mmol/g)'], index=range(0, 100))

    # Write attributes
    df_output['Experiment Attribute'].iloc[0] = 'Material'
    df_output['Experiment Attribute'].iloc[1] = 'Adsorbate'
    df_output['Experiment Attribute'].iloc[2] = 'Temperature'

    df_output['Value'].iloc[0] = material
    df_output['Value'].iloc[1] = adsorbate
    df_output['Value'].iloc[2] = temperature + ' C'


    # Read pressure and loading values
    pressure_points = df['5'].iloc[df[df['5'] == 'Pc2 (Peq)'].index.item() + 1:].reset_index(drop=True)
    loading = df['16'].iloc[df[df['16'] == 'Nexc/g'].index.item() + 1:].reset_index(drop=True)
    loading = pd.to_numeric(loading)
    pressure_points = pd.to_numeric(pressure_points)

    # Write pressure and loading values
    df_output['Pressure (bar)'] = pressure_points
    df_output['Loading (mmol/g)'] = loading*1000

    # Export output file
    df_output.to_csv('.\\output\\'+item.split('.')[0]+'.csv', index=None)
