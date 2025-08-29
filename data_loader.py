import pandas as pd

def carregar_dados(path='Datas\data_orbitas.parquet'):
    df = pd.read_parquet(path)
    unique_valors = sorted(df["N"].unique())
    return df, unique_valors