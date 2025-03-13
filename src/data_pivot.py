# 📂 src/data_pivot.py - Pivotación y transformación de datos

import pandas as pd
from data_selection import select_data

def pivot_data():
    df = select_data()
    df_pivot = df.pivot_table(index='Pais', columns='Mes', values='Ventas', aggfunc='sum')
    df_pivot.to_csv("data_pivot.csv")
    return df_pivot

if __name__ == "__main__":
    pivot_data()