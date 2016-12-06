import pandas as pd
import seaborn as sns
import os
import glob
import matplotlib.pyplot as plt

path = 'C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/datavis/12'
styles = ['Value', 'Leverage', 'Growth', 'Size', 'Volatility', 'Liquidity', 'Exchange Rate Sensitivity']
all_files_return = glob.glob(os.path.join(path, 'AXWW21-MH.*.ret')) # advisable to use os.path.join as this makes concatenation OS independent
all_files_exp = glob.glob(os.path.join(path, 'AXWW21-MH.*.exp'))

#Dates - list comprehension
dates = [pd.to_datetime(filepath[-12:-4], format = '%Y%m%d') for filepath in all_files_return]
#   count = 0

return_df = pd.DataFrame()

for file_ in all_files_return:
   # df = pd.read_table('file:///C:/Users/cpattapagala/PycharmProjects/PythonLessons/PythonScrapFiles/datavis/12/AXWW21-MH.20151201.ret', skiprows=range(3), sep='|', names = ['FactorName', 'Return', 'Cumulative Return'], header= None, verbose=True)
#    count = count + 1

    df = pd.read_table(file_, skiprows=range(3), sep='|', names = ['FactorName', 'Return', 'Cummulative Return'], header= None, verbose=False)
    #Can be scalable
    return_df = return_df.append(df['Return'].transpose())

#indexing and column names
return_df.columns = df['FactorName'].transpose()
return_df.index = dates
return_df.columns.name = ''
return_df.index.name = 'Date'

for exp_file in all_files_exp:
    df = pd.read_table(exp_file, skiprows=range(2), sep = '|', verbose=False)


#  Data Visualization
'''
melt works by taking observations that are spread across columns (away_team, home_team), and melting them down into one column with multiple rows. However, we don't want to lose the metadata (like game_id and date) that is shared between the observations. By including those columns as id_vars, the values will be repeated as many times as needed to stay with their observations.
'''

#Plotting
plt.close('all')
fig, ax = plt.subplots(1)
plt.grid(True)
ax.plot(return_df[styles])
fig.autofmt_xdate()

import matplotlib.dates as mdates
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

#Exposures distribution
