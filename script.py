from garminconnect import Garmin
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import csv

dates = []
start_date = datetime(2024, 12, 21)
end_date = datetime.now()
delta = timedelta(days=1)
current_date = start_date

while current_date <= end_date:
    date = current_date.strftime("%Y-%m-%d")
    current_date += delta
    dates.append(date)

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

client = Garmin(email=email, password=password)
client.login()

for date in dates:
    heart_rates_data = client.get_heart_rates(cdate=date)
    data = heart_rates_data['heartRateValues']

    with open(f"data/raw/{date}.csv", "w", newline="") as file:
        fieldnames = ['timestamp', 'heart_rates']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for x in data:
            timestamp, heart_rates = x[0], x[1]
            timestamp = timestamp / 1000
            dt = datetime.fromtimestamp(timestamp).strftime("%H:%M")

            writer.writerow({'timestamp': dt, 'heart_rates': heart_rates})


            

