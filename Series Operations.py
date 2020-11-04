import pandas as pd
import numpy as np

data=np.random.randn(5)
test_data=pd.Series(data)
test_data.index=['A','B','C','D','E']
print(test_data)

#Slicing
Top_Three=test_data[:3]
print(Top_Three)