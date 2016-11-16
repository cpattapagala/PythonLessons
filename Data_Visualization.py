import pandas as pd
import seaborn as sns
import os
import glob
import matplotlib.pyplot as plt

path = 'C:/Users/cpattapagala/PycharmProjects/PythonLessons/PythonScrapFiles/datavis/12'

all_files = glob.glob(os.path.join(path, "AXWW21-MH.*.ret")) # advisable to use os.path.join as this makes concatenation OS independent

#Dates - list comprehension
dates = [pd.to_datetime(filepath[-12:-4], format = '%Y%m%d') for filepath in all_files]
#   count = 0

return_df = pd.DataFrame()

for file_ in all_files:
    #df = pd.read_table('file:///C:/Users/cpattapagala/PycharmProjects/PythonLessons/PythonScrapFiles/datavis/12/AXWW21-MH.20151201.ret', skiprows=range(3), sep='|', names = ['FactorName', 'Return', 'Cumulative Return'], header= None, verbose=True)
#    count = count + 1

    df = pd.read_table(file_, skiprows=range(3), sep='|', names = ['FactorName', 'Return', 'Cummulative Return'], header= None, verbose=False)
    #Can be scalable
    return_df = return_df.append(df['Return'].transpose())


#indexing and column names
return_df.columns = df['FactorName'].transpose()
return_df.index = dates
return_df.columns.name = ''
return_df.index.name = 'Date'

#  Data Visualization
'''
melt works by taking observations that are spread across columns (away_team, home_team), and melting them down into one column with multiple rows. However, we don't want to lose the metadata (like game_id and date) that is shared between the observations. By including those columns as id_vars, the values will be repeated as many times as needed to stay with their observations.
'''

df = pd.melt(return_df.reset_index(), id_vars=['Date'], var_name='Factor Name')

#Plotting

df1 = df.groupby(["Factor Name", "Date"]).mean().unstack("Factor Name").plot()
