import pandas as pd

#read csv file
data = pd.read_csv('sample.csv')

#select specific rows and columns
data_new = data.iloc[1:,[0,1]]
#or
# data_new = data.iloc[:3,[0,1]].copy()

# update entry
data_new.iloc[2,1] = 100


#save as csv
data_new.to_csv('output.csv')


