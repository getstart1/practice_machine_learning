import pandas as pd

#read dataset using panda libriary
ds = pd.read_csv("/Users/qdai/Desktop/machine_learning_practice/linear regression/Salary.csv")

print(ds.head(1))
print(ds['Salary'].dtypes)
