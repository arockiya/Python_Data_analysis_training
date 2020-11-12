# Create a DataFrame using Numpy
import pandas as pd
import numpy as np

dates = pd.date_range('today',periods=6) # this will create last six days from today
num_arr=np.random.randn(6,5) # this will generate random 6 rows 4 columns data
Columns=['Col1','Col2','Col3','Col4','Col5']
df1=pd.DataFrame(num_arr,index=dates,columns=Columns)
print(df1)

# Create a DataFrame using Dictionary

dict={'Year':[2014,2014,2014,2014,2015,2015,2015,2015],
      'Region':['East','West','North','South','East','West','North','South'],
      'Revenue':[80191,80773,59707,39796,68100,98456,84487,95793]}
id=[1,2,3,4,5,6,7,8]
df2=pd.DataFrame(dict,index=id)
print(df2)

print(df2.T)

print(df2.sort_values(by="Revenue"))

print(df2[1:3])

# Query the data frame
print(df2[['Year','Revenue']])

# copy the whole data frame

df3=df2.copy()
print(df3)

# to find Null values
print(df2.isnull())

# to change the value in particular cell
df3.loc['1','Revenue']=85000
print(df3)

#mean
print(df3.mean())

#sum
print(df3['Revenue'].sum())

