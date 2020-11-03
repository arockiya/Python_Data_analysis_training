import pandas as pd
print("Pandas imported")

#data=pd.read_csv('Resources/pokemon_data.csv')
#print(data)

d_xlsx=pd.read_excel('Resources/pokemon_data.xlsx',sheet_name='pokemon_data')
#print(d_xlsx)

# Top 5
print(d_xlsx.head(5))

# Bottom 5
#print(d_xlsx.tail(5))