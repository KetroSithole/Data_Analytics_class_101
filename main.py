import pandas as pd

# df = pd.read_csv("student-mat.csv")
with open("student-mat.csv", 'r') as file:
    content = file.read()
    print(content)

# print(df.head())
# print(df.columns.to_list())

import csv
data = list(csv.reader(open("student-mat.csv", 'r'), delimiter=";"))
print(data)
