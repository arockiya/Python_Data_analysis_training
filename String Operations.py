import pandas as pd
import numpy as  np

string=pd.Series(['A','C','D','Aaa','BaCa',np.nan,'CBA','Cow','owl'])
print(string)

# lower
print(string.str.lower())

# upper
print(string.str.upper())