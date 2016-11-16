import pandas as pd
import zipfile

zf = zipfile.ZipFile("C:/Users/cpattapagala/Downloads/531398784_T_ONTIME.zip")
filename = zf.filelist[0].filename

fp = zf.extract(filename)
df = pd.read_csv(fp, parse_dates="FL_DATE").rename(columns=str.lower)

df.head()


'''The first row of each group is given my first() function'''
first = df.groupby('airline_id')[['fl_date', 'unique_carrier']].first()

