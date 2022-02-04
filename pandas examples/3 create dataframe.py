import pandas as pd

a = [['a',11,1000],['b',22,1200],['c',32,1300]]

#create data frame using list
df1 = pd.DataFrame(a)

print(df1)

#create dataframe with header
df2 = pd.DataFrame(a, columns = ['M','N','K'], index = [101,102,105])

print(df2)