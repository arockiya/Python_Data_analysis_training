# Basic operations on Pandas Series

### Slicing

In slicing, we can get the data from index number to index number.
For we can get the top three rows based on Index number.
> series_name[start_index:end_index]

> *Index number will start with 0*

In a five row series, the start_index for the first row is Zero. Whereas end_index of 5th row is 4 __(not 5)__.

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

### Append (Qlik: Concatenate)
It will add two seperate series one after another.
> series1.append(series2)

    # Append
    data2=np.random.randn(5)
    test_data2=pd.Series(data2)
    series3=test_data.append(test_data2)
    print(series3)
    
    A   -0.173296
    B   -0.244840
    C    0.383916
    D   -0.214927
    E    1.401547
    0    1.541731
    1    1.577715
    2   -1.818096
    3   -1.311908
    4   -0.246267
    dtype: float64
    
# Numerical Operations
To perform numerical operations, the index numbers must be in numericals. 

### 1. Addition
> series1.add(series2)

This will just add the two series values based on the index number. i.e., value of index 0 in series1 + value of index 0 in series 2
    
    add = test_data.add(test_data2)
    print(add)
    
    0    1.404036
    1    1.194439
    2    0.930011
    3   -0.188143
    4   -1.254986
    
### 2. Subtraction
> series1.sub(series2)

This will just subtract the two series values based on the index number. i.e., value of index 0 in series1 - value of index 0 in series 2.

    sub=test_data.sub(test_data2)
    print(sub)
    
    0   -1.097665
    1   -1.497920
    2   -2.056519
    3   -1.731232
    4    0.410954
    dtype: float64
    
### 3. Multiply
> series1.mul(series2)

This will multiply the two series values based on the index number. i.e., value of index 0 in series1 * value of index 0 in series 2

    mul=test_data.mul(test_data2)
    print(mul)
    
    0    0.081666
    1   -1.017924
    2    0.083885
    3   -0.178226
    4   -0.770339
    dtype: float64
    
### 4. Division
> series1.div(series2)

This will divide the two series values based on the index number. i.e., value of index 0 in series1 / value of index 0 in series 2.

If divide by zero, then, *inf* value will be returned and one of the series have less rows than the other, the *NaN* value will be returned.

    div=test_data.div(test_data2)
    print(div)
    
    0    1.702539
    1   -0.200545
    2    0.874735
    3    1.390366
    4    2.540514
    dtype: float64

### 5.Median

    print('Median: ',test_data.median())
    
    Median:  -0.48549679479782726
    
### 6. Maximum

    print('Median: ',test_data.max())
    
    Median:  1.2420990049503244
    
### 7. Minimum

    print('Median: ',test_data.min())
    
    Median:  -0.7339671837327253