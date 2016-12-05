import pandas as pd
import seaborn as sns
import os
import glob
import matplotlib.pyplot as plt

path = 'C:/Users/cpattapagala/PycharmProjects/PythonLessons/PythonScrapFiles/datavis/12'
all_files = glob.glob(os.path.join(path, 'AXWW21-MH.*.exp'))

#Dates - List Comprehension
dates = [pd.to_datetime(filepath[-12:-4], format = '%Y%m%d') for filepath in all_files]

exp_df = pd.read_table(all_files[1], skiprows=range(4), sep='|', header=None,  names= ['AxiomaID', 'Global Market', 'Value', 'Leverage', 'Growth', 'Size', 'Short-Term Momentum', 'Medium-Term Momentum', 'Volatility', 'Liquidity', 'Exchange Rate Sensitivity'], verbose=False, usecols=range(11))
exp_indexed = exp_df.set_index('AxiomaID').fillna(0)

sns.set(color_codes=True)

for col_id in exp_indexed.columns:
    sns.distplot(exp_indexed[col_id])