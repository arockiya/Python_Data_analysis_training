# Data Frames in Python

__Definition from Pandas wiki__

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

###  Create a DataFrame

To create a Data Frame, we need the following things.
1. Index Field - Like a Timestamp or Primary key or a rowid
2. Column Field - Column names
3. Actual Values - Data

__Create a Data frame using Numpy__

    dates = pd.date_range('today',periods=6) # this will create last six days from today
    print(dates)
    
    DatetimeIndex(['2020-11-09 07:41:24.675800', '2020-11-10 07:41:24.675800',
               '2020-11-11 07:41:24.675800', '2020-11-12 07:41:24.675800',
               '2020-11-13 07:41:24.675800', '2020-11-14 07:41:24.675800'],
              dtype='datetime64[ns]', freq='D')
              
Actual code

    dates = pd.date_range('today',periods=6) # this will create last six days from today
    num_arr=np.random.randn(6,5) # this will generate random 6 rows 4 columns data
    Columns=['Col1','Col2','Col3','Col4','Col5']
    df1=pd.DataFrame(num_arr,index=dates,columns=Columns)
    print(df1)
    
                                    Col1      Col2      Col3      Col4      Col5
    2020-11-09 07:44:19.975113  0.787829 -0.868306 -2.035698 -0.686477  0.603144
    2020-11-10 07:44:19.975113 -0.804743 -0.330908  1.753301  0.119184  0.584015
    2020-11-11 07:44:19.975113 -0.523709 -1.370821 -0.523984  0.345989 -0.018601
    2020-11-12 07:44:19.975113  0.434697 -0.962571  0.389638  0.349281 -0.767048
    2020-11-13 07:44:19.975113  0.806045  0.035346  1.381410 -0.846861 -2.037842
    2020-11-14 07:44:19.975113 -1.116785  0.886561 -0.183179  0.974298  1.233438

__Create a DataFrame using Dictionary__

    dict={'Year':[2014,2014,2014,2014,2015,2015,2015,2015],
      'Region':['East','West','North','South','East','West','North','South'],
      'Revenue':[80191,80773,59707,39796,68100,98456,84487,95793]}
    id=[1,2,3,4,5,6,7,8]
    df2=pd.DataFrame(dict,index=id)
    print(df2)
    
       Year Region  Revenue
    1  2014   East    80191
    2  2014   West    80773
    3  2014  North    59707
    4  2014  South    39796
    5  2015   East    68100
    6  2015   West    98456
    7  2015  North    84487
    8  2015  South    95793