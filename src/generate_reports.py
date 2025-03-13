# 📂 src/generate_reports.py - Generación de reportes en HTML con gráficos

import pandas as pd
import plotly.express as px

def generate_html_report():
    df = pd.read_csv("data_pivot.csv")
    fig = px.bar(df, x=df.columns[0], y=df.columns[1:])
    fig.write_html("report.html")
    print("Reporte generado.")

if __name__ == "__main__":
    generate_html_report()