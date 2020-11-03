# Pandas series

List in python is simple list used to store the values.

    arr=[1,2,3,4]
    print(arr)
    
    [1, 2, 3, 4]
    
Series is Pandas is like tables with indexes. By default the index will start with zero.
    
    s1=pd.Series(arr)
    print(s1)

    0    1
    1    2
    2    3
    3    4
    dtype: int64
