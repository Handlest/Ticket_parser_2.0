import plotly.graph_objs as go
import sqlite3
connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()
def company(company, fr='LED', to='MOW'):
    try:
        cursor.execute(f'SELECT value, depart_date'
                       f' FROM tickets'
                       f' WHERE gate = ? AND origin = "LED" AND destination = "MOW"'
                       f' ORDER BY depart_date',
                       (company, ))
        records = list(zip(*cursor.fetchall()))
        fig = go.Figure()
        print("Всего строк подходящих под условие: ", len(records[0]))
        fig.add_trace(go.Scatter(x=records[1], y=records[0], name='price', mode='lines+markers'))
        fig.update_layout(title=f'Цены на авиабилеты компании {company} из {fr} в {to}', xaxis_title='День вылета',
                          yaxis_title='Цена, руб', margin=dict(l=0, r=0, t=40, b=0))
        fig.show()
    except Exception as ex:
        print(ex)

def date_range(start, end, fr='LED', to='MOW'):
    cursor.execute(f'SELECT value, depart_date'
                   f' FROM tickets'
                   f' WHERE depart_date BETWEEN ? AND ? AND origin = "LED" AND destination = "MOW"'
                   f' ORDER BY depart_date',
                   (start, end))
    records = list(zip(*cursor.fetchall()))
    print("Всего строк подходящих под условие: ", len(records[0]))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=records[1], y=records[0], name='price', mode='lines+markers'))
    fig.update_layout(title=f'Цены на авиабилеты из {fr} в {to} с {start} по {end}', xaxis_title='День вылета',
                      yaxis_title='Цена, руб', margin=dict(l=0, r=0, t=40, b=0))
    fig.show()






date_range("2022-01-10", "2023-05-15", 'MOW', 'LED')