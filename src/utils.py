import os
from datetime import datetime, timedelta

from pathlib import Path
from dateutil import parser


class Utils:
    is_print = True

    @staticmethod
    def load_envs():
        from dotenv import load_dotenv
        found = load_dotenv()
        print("loaded .env:", found)
        print("key present:", bool(os.environ.get("Example key")))

    @staticmethod
    def store_data(df, file_name):
        data_dir = Path("data")
        data_dir.mkdir(parents=True, exist_ok=True)
        output_file = data_dir / "2024.csv"
        df.to_csv(output_file, index=False)
        print(df)

    @classmethod
    def is_weekend(cls, date_str):
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            cls.dprint(date.strftime("%Y-%m-%d"))
            return date.weekday() >= 5
        else :
            return ''

    @staticmethod
    def extract_date(date_str):

        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        last_week = today - timedelta(weeks=1)  # Or timedelta(days=7)
        next_week = today + timedelta(weeks=1)  # Or timedelta(days=7)
        fortnight_ago = today - timedelta(days=14)
        fortnight_later = today + timedelta(days=14)

        if 'today' in date_str:
            print(today)
            return str(today)
        elif 'yesterday' in date_str:
            return str(yesterday)
        elif 'tomorrow' in date_str:
            return str(tomorrow)
        elif 'last week' in date_str:
            return str(last_week)
        elif  'next week' in date_str:
            return str(next_week)
        elif 'fortnight ago' in date_str:
            return str(fortnight_ago)
        elif 'fortnight later' in date_str:
            return str(fortnight_later)
        else:
            try :
                dt = parser.parse(date_str, fuzzy=True)
                date = dt.strftime("%Y-%m-%d")
                return date
            except (ValueError) :
                return False

    @classmethod
    def dprint(cls, string):
        if cls.is_print:
            print(string)
        else:
            pass







