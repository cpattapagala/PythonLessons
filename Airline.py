import zipfile

import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# For the blog, I've truncated an obscenely long url.
# Download the notebook if you're following along.
data = 'UserTableName=On_Time...'

r = requests.post('http://www.transtats.bts.gov/DownLoad_Table.asp?Table_ID=236&Has_Group=3&Is_Zipped=0',
                  data=data, stream=True)

with open("flights.csv", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

zf = zipfile.ZipFile("flights.csv.zip")
filename = zf.filelist[0].filename
fp = zf.extract(filename)
df = pd.read_csv(fp, parse_dates="FL_DATE").rename(columns=str.lower)

df.head()
