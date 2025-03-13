import pandas as pd

def modifySalaryColumn(employees):
    employees['salary'] = employees['salary'] * 2
    return employees
