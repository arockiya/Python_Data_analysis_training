import pandas as pd
print("Pandas imported")

data=pd.read_csv('Resources/pokemon_data.csv')
print(data)

# Top 5
print(data.head(5))

# Bottom 5
print(data.tail(5))