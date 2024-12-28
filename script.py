from garminconnect import Garmin
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

client = Garmin(email=email, password=password)
client.login()