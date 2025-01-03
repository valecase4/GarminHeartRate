from garminconnect import Garmin
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import csv
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

client = Garmin(email=email, password=password)
client.login()

dates = []
start_date = datetime(2024, 12, 21)
end_date = datetime.now()
delta = timedelta(days=1)
current_date = start_date

while current_date <= end_date:
    date = current_date.strftime("%Y-%m-%d")
    current_date += delta
    dates.append(date)

def fetch_heart_rate_data(date, max_retries=5):
    retries = 0
    delay = 1 
    while retries < max_retries:
        try:
            heart_rates_data = client.get_heart_rates(cdate=date)
            return heart_rates_data
        except Exception as e:
            retries += 1
            logging.warning(f"Errore durante la richiesta per {date}: {e}. Tentativo {retries}/{max_retries}")
            time.sleep(delay)
            delay *= 2
    logging.error(f"Impossibile ottenere i dati per {date} dopo {max_retries} tentativi.")
    return None

def fetch_sleep_data(date, max_retries=5):
    retries = 0
    delay = 1
    while retries < max_retries:
        try:
            sleep_data = client.get_sleep_data(cdate=date)
            return sleep_data
        except Exception as e:
            retries += 1
            logging.warning(f"Errore durante la richiesta per {date}: {e}. Tentativo {retries}/{max_retries}")
            time.sleep(delay)
            delay *= 2
    logging.error(f"Impossibile ottenere i dati per {date} dopo {max_retries} tentativi.")
    return None

for date in dates:
    logging.info(f"Estrazione dati per {date}...")
    heart_rates_data = fetch_heart_rate_data(date)
    sleep_data = fetch_sleep_data(date)

    if not heart_rates_data:
        logging.error(f"Dati mancanti per {date}. Procedo con il giorno successivo.")
        continue

    if not sleep_data:
        logging.error(f"Dati mancanti per {date}. Procedo con il giorno successivo.")
        continue

    data1 = heart_rates_data['heartRateValues']
    file_path_1 = f"data/raw/heart_rates/{date}.csv"

    with open(file_path_1, "w", newline="") as file:
        fieldnames = ['timestamp', 'heart_rates']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for x in data1:
            timestamp, heart_rates = x[0], x[1]
            timestamp = timestamp / 1000
            dt = datetime.fromtimestamp(timestamp).strftime("%H:%M")
            writer.writerow({'timestamp': dt, 'heart_rates': heart_rates})

    logging.info(f"Dati salvati per {date}: {file_path_1}")

    data2 = sleep_data['sleepLevels']
    file_path_2 = f"data/raw/sleep/{date}.csv"

    with open(file_path_2, "w", newline="") as file:
        fieldnames = ['start_time', 'end_time', 'sleep_type']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for x in data2:
            start_time = x['startGMT']
            end_time = x['endGMT']
            sleep_type = x['activityLevel']
            writer.writerow({'start_time': start_time, 'end_time': end_time, 'sleep_type': sleep_type})

# for record in client.get_sleep_data(cdate='2024-12-23')['sleepLevels']:
#     print(record)