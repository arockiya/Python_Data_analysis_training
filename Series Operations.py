import pandas as pd
import numpy as np

data=np.random.randn(5)
test_data=pd.Series(data)
#test_data.index=['A','B','C','D','E']
print(test_data)

#Slicing
Top_Three=test_data[:3]
print(Top_Three)

bottom_two=test_data[3:]
print(bottom_two)

top_three2=test_data[:-2]
print(top_three2)

# Append
data2=np.random.randn(5)
test_data2=pd.Series(data2)

series3=test_data.append(test_data2)
print(series3)

# Addition
add = test_data.add(test_data2)
print(add)

# Subtraction
sub=test_data.sub(test_data2)
print(sub)

# Multiply
mul=test_data.mul(test_data2)
print(mul)

# Division
div=test_data.div(test_data2)
print(div)

# Median
print('Median: ',test_data.median())

# Max
print('Median: ',test_data.max())

# Min
print('Median: ',test_data.min())