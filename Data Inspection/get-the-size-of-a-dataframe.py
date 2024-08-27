import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    l=[]
    l.append(len(players))
    l.append(len(players.columns))
    return l
    
    
