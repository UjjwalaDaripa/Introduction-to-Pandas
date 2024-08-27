import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers['rank']=customers.groupby('email')['customer_id'].rank(method='min')
    df=customers[['customer_id','name','email']].where(customers['rank']==1)
    df=df.dropna()
    return(df)
