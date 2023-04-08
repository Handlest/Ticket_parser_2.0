import datetime
import requests
import pandas as pd


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
