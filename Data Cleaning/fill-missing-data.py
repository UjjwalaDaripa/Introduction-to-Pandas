import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].case_when([
    (products["quantity"].isna(), 0)
    ])
    return products
    
