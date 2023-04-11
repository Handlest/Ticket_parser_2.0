# API token is e792af02824136cab4885087552040fc
import time
import datetime
import schedule
import sqlite3
import requests
import pandas as pd


connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()



def get_month_prices():
    URL = 'http://api.travelpayouts.com/v2/prices/month-matrix?currency=rub&origin=LED&destination=MOW' \
          '&show_to_affiliates=true&token=e792af02824136cab4885087552040fc'
    response = requests.get(URL).json()
    if response['success']:
        df = pd.json_normalize(response, record_path='data')
        return df
    else:
        with open('log.txt') as log_file:
            log_file.writelines(f'Ошибка при сборе информации. {response["error"]}. Время: {str(datetime.datetime.now())}')

def parse_and_write():
    data = get_month_prices()
    data.to_sql('tickets', connection, if_exists='append', index=False)

def main():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS tickets(value, trip_class, show_to_affiliates, origin, destination, gate,'
        'depart_date, return_date, number_of_changes, found_at, duration, distance, actual)')
    parse_and_write()


if __name__ == '__main__':
    schedule.every().monday.at("10:00").do(main)
    schedule.every().wednesday.at("10:00").do(main)
    schedule.every().friday.at("10:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)