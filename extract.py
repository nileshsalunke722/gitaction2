import pandas as pd
print("Extracting data from SQL...")

dict = {
    "id":[1, 2, 3],
    "name":["A","B","C"],
    "age":[10,20,30]
}

df=pd.DataFrame(dict)
print(df)