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
We can change the indexing number by creating a one more list for index order and pass it inside the Series function like below.

    indexorder = [4,3,2,1]
    s2=pd.Series(arr,index=indexorder)
    print(s2)
    
    4    1
    3    2
    2    3
    1    4
    dtype: int64 
> Number of objects in the Series should be equal to number of index values.

### Create a random series using Numpy
We can create a Series with random number using numpy very easily.

    # create a series with random values
    import numpy as np
    test = np.random.randn(5)
    print(test)
    
    [ 1.43355486 -0.07554014  0.03412132 -0.24848293  1.08147963]
    
    s3=pd.Series(test)
    
    0    1.433555
    1   -0.075540
    2    0.034121
    3   -0.248483
    4    1.081480
    dtype: float64
    
### Create a series using dictionary
We can create a series using dictionary as well.

    d = {'A':1,'B':2,'C':3,'D':4}
    s4=pd.Series(d)
    print(s4)
    
    A    1
    B    2
    C    3
    D    4
    dtype: int64


