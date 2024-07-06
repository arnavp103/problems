# 2878 Get the Size of a DataFrame

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)
