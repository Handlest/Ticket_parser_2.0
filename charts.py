import plotly.graph_objs as go
import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()
def build_chart():
    cursor.execute('SELECT * FROM tickets WHERE gate = "Победа" ORDER BY depart_date')
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    prices = []
    dates = []
    for row in records:
        prices.append(row[0])
        dates.append(row[6])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=prices))
    fig.show()

build_chart()