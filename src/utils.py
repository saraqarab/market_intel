import os
from datetime import datetime
import dateparser as dp
from pathlib import Path
from dateutil import parser

is_print = True


def dprint(string):
    if is_print is True:
        print(string)
    else:
        pass

class Utils:
    def load_envs(self):
        from dotenv import load_dotenv
        found = load_dotenv()
        print("loaded .env:", found)
        print("key present:", bool(os.environ.get("Example key")))

    def store_data(self, df, file_name):
        data_dir = Path("data")
        data_dir.mkdir(parents=True, exist_ok=True)
        output_file = data_dir / "2024.csv"
        df.to_csv(output_file, index=False)
        print(df)

    def is_weekend(self, date_str):
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            dprint(date.strftime("%Y-%m-%d"))
            return date.weekday() >= 5
        else :
            return ''

    def extract_date(self, date_str):
        dt = parser.parse(date_str, fuzzy=True)
        if dt:
            date = dt.strftime("%Y-%m-%d")
            return date
        else:
            return False







