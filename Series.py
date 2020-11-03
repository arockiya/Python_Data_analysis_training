import  pandas as pd
print("Pantas imported")

arr=[1,2,3,4]
print(arr)

s1=pd.Series(arr)
print(s1)

indexorder = [4,3,2,1]
s2=pd.Series(arr,index=indexorder)
print(s2)

# create a series with random values
import numpy as np
test = np.random.randn(5)
print(test)
s3=pd.Series(test)
print(s3)

# create a series with dictionary
d = {'A':1,'B':2,'C':3,'D':4}
s4=pd.Series(d)
print(s4)