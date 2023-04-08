# API token is e792af02824136cab4885087552040fc
# Partner marker is 419542
import schedule
from functions import get_month_prices
import sqlite3

def parse_and_write():
    data = get_month_prices()
    for i in range(data.shape[0]):
        tmp = tuple(data.iloc[[i]].values.tolist()[0])
        cursor.execute(f"INSERT INTO tickets VALUES {tmp}")
        connection.commit()

# res = cursor.execute("PRAGMA table_info('tickets')")
# column_names = [i[1] for i in cursor.fetchall()]
# print(column_names)  # Выводит список столбцов в указанной таблице

# cursor.execute('CREATE TABLE tickets(value, trip_class, show_to_affiliates, origin, destination, gate, depart_date,'
#                'return_date, number_of_changes, found_at, duration, distance, actual)')  # Создаёт таблицу с заданными полями

# result = cursor.execute('SELECT name FROM sqlite_master')  # Выводит имена всех таблиц в базе
# print(result.fetchone())

# for i in range(data.shape[0]):
#     tmp = tuple(data.iloc[[i]].values.tolist()[0])
#     cursor.execute(f"INSERT INTO tickets VALUES {tmp}")
#     connection.commit()

# res = cursor.execute("SELECT * FROM tickets")
# print(res.fetchall())  # Выводит всю информацию из таблицы


if __name__ == '__main__':
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    names = cursor.execute('SELECT name FROM sqlite_master')
    if 'tickets' not in names:
        cursor.execute('CREATE TABLE tickets(value, trip_class, show_to_affiliates, origin, destination, gate, depart_date,'
                       'return_date, number_of_changes, found_at, duration, distance, actual)')
    else:
        parse_and_write()
