import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=animals[['name','weight']].where(animals['weight']>100)
    df=df.sort_values(by=['weight'],ascending=False)
    df=df.dropna()
    df1=df[['name']]
    return df1
    
