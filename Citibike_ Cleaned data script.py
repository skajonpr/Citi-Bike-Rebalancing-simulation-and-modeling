# -*- coding: utf-8 -*-
"""

@author: Sukit Kajonpradapkul

Description: This file is to clean an organized dataset derived from the open bus website which periodically collected station status from Citibike database.

"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

citibike = []

with open('bikeshare_nyc_raw (2).csv') as files:
    reader = csv.reader(files)
    
    citibike = [i[0] for i in reader]
   

citibike = [i.strip().replace('\t', ',').replace('\\','') for i in citibike ]    


frame = []

for i in citibike:
    _list = [] 
    _list.append(i)
    frame.append(_list)
    
split_frame = [i[0].split(',') for i in frame  ]

    
    
df = pd.DataFrame(np.array(split_frame))
df_519 = df[df[0]== '519']


filtered_df = df_519.filter(items = [2,3,4,5,6])
filter_date_df = filtered_df[filtered_df[3] >= '5'] 
filter_date_df = filter_date_df[filter_date_df[3] <= '7']
filter_date_df = filter_date_df[filter_date_df[5] >= '1'] 
filter_date_df[0] = '.'
filter_date_df[1] = filter_date_df[3].str.cat(filter_date_df[0])
filter_date_df[7] = filter_date_df[1].str.cat(filter_date_df[4])
filter_date_df.drop(columns = [0,1])

#filter_date_df = filter_date_df[filter_date_df[2] == '"18-07-11"']
filter_date_df[6] = filter_date_df[6].astype(float)
filter_date_df[7] = filter_date_df[7].astype(float)
ax1 = filter_date_df.plot.scatter(x= [7], y= [6],c='DarkBlue')
plt.title('Bike level at Pershing Square North (Actual data of July 2018)')
plt.xlabel('Time (5 pm - 8 pm)')
plt.ylabel('Bike Levels')
plt.savefig('scatter_.png')


# import cleaned data to Excel file.
writer = pd.ExcelWriter('citibike_201807_519.xlsx',  engine = 'xlsxwriter')
df_519.to_excel(writer,'Sheet1')    
writer.save()
