import pandas as pd

def concatenateTables(df1, df2):
    result = pd.concat([df1, df2], ignore_index=True)
    return result
