import pandas as pd

def changeDatatype(students):
    students['grade'] = students['grade'].astype(int)
    return students
