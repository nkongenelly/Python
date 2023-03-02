import pandas as pd

file1 = r'/mnt/d/Code/GE/cross_validation/data/Book1.csv'
df1 = pd.read_csv(file1)
print(df1)

file2 = r'/mnt/d/Code/GE/cross_validation/data/Book2.csv'
df2 = pd.read_csv(file2)
print(df2)
print('hello')

# print(df2.columns)
df_master = df1.merge(df2, on="AccountID", how="inner")
print(df_master)