# 📂 src/data_selection.py - Selección de datos desde SQL Server

import pyodbc
import pandas as pd

def select_data():
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=tu_servidor;DATABASE=tu_db;UID=usuario;PWD=contraseña")
    query = "SELECT * FROM Ventas"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    data = select_data()
    print("Datos seleccionados:", data.head())