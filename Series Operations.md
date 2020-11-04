# Basic operations on Pandas Series

### Slicing

In slicing, we can get the data from index number to index number.
For we can get the top three rows based on Index number.
> series_name[start_index:end_index]

If end_index is negative, that means (total-number). If a series have 5 values, end_index -2 means till 3rd row.

    import pandas as pd
    import numpy as np

    data=np.random.randn(5)
    test_data=pd.Series(data)
    test_data.index=['A','B','C','D','E']

    #Slicing
    Top_Three=test_data[:3]
    print(Top_Three)
 
    A    0.068615
    B   -0.162466
    C    1.096466
    dtype: float64