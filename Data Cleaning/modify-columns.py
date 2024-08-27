import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    #customers['rank']=customers.groupby('email')['customer_id'].rank(method='min')
    employees['salary']=employees['salary']*2
    return employees
