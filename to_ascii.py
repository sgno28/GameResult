import pandas as pd
from prettytable import PrettyTable 
#use this code if your table is already formatted
df = pd.read_csv("Game_Results_24_MAY.csv")

table = PrettyTable()
headers = []
for cols in df.columns:
    headers.append(cols)

table.field_names = headers

for i in range(0, len(df)):
    row = df.loc[i].values.flatten().tolist()
    table.add_row(row)

print(table)