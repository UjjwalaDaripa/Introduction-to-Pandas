import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    #customers['rank']=customers.groupby('email')['customer_id'].rank(method='min')
    df=students.where(students['name'].isna()==False)
    df=df.dropna(how='all')
    return df
    
