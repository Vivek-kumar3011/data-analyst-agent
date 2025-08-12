import pandas as pd
import os

def load_data(file_paths):
    dfs = []
    for path in file_paths:
        if path.endswith(".csv"):
            dfs.append(pd.read_csv(path))
        elif path.endswith(".parquet"):
            dfs.append(pd.read_parquet(path))
        # Extend for JSON, Excel, etc.

    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return pd.DataFrame()
