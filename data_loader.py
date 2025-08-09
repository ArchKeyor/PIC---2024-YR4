import pandas as pd

pd.set_option('display.max_columns', None)

def carregar_dados(path='data_orbitas.sal'):
    with open("data_orbitas.sal", "r") as f:
        lines = f.readlines()

    columns = (lines[0].strip().split()) + (lines[1].strip().split())
    data = []
    tempo = sobrevivientes = None

    for line in lines[2:]:
        tokens = line.strip().split()
        if len(tokens) == 2:
            tempo = float(tokens[0])
            sobrevivientes = int(tokens[1])
        elif len(tokens) == 7 and tempo is not None:
            row = [tempo, sobrevivientes] + [float(x) for x in tokens]
            data.append(row)

    df = pd.DataFrame(data, columns=columns)
    return df, sorted(df["N"].unique())