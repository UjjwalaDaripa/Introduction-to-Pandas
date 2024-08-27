import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    table = pd.pivot_table(weather, values ='temperature', index =['month'], 
                         columns =['city']) 
    return table
