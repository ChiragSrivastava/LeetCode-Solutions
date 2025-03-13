import pandas as pd

def meltTable(report):
    result = report.melt(id_vars=["product"], 
                         var_name="quarter", 
                         value_name="sales")
    return result
