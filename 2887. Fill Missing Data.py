import pandas as pd

def fillMissingValues(products):
    products['quantity'] = products['quantity'].fillna(0)
    return products
