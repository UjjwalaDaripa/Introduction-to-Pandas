import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=students[['name','age']].where(students['student_id']==101)
    df=df.dropna()
    return df
    
