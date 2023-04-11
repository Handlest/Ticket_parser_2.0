# API token is e792af02824136cab4885087552040fc
# Partner marker is 419542
import time
from functions import get_month_prices
import schedule
import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

def parse_and_write():
    data = get_month_prices()
    for i in range(data.shape[0]):
        tmp = tuple(data.iloc[[i]].values.tolist()[0])
        cursor.execute(f"INSERT INTO tickets VALUES {tmp}")
        connection.commit()

def main():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS tickets(value, trip_class, show_to_affiliates, origin, destination, gate,'
        'depart_date, return_date, number_of_changes, found_at, duration, distance, actual)')
    parse_and_write()


if __name__ == '__main__':
    schedule.every().monday.at("10:15").do(main)
    schedule.every().wednesday.at("10:15").do(main)
    schedule.every().friday.at("10:15").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)