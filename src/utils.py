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
        output_file = data_dir / file_name
        df.to_csv(output_file, index=False)
        return output_file

    @classmethod
    def is_weekend(cls, date_str):
        if not date_str:
            return False
        date = datetime.strptime(str(date_str)[:10], "%Y-%m-%d")
        cls.dprint(date.strftime("%Y-%m-%d"))
        return date.weekday() >= 5

    @staticmethod
    def extract_date(question):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        last_week = today - timedelta(weeks=1)
        next_week = today + timedelta(weeks=1)
        fortnight_ago = today - timedelta(days=14)
        fortnight_later = today + timedelta(days=14)
        question_lower = question.lower()

        if "today" in question_lower:
            return today.strftime("%Y-%m-%d")
        if "yesterday" in question_lower:
            return yesterday.strftime("%Y-%m-%d")
        if "tomorrow" in question_lower:
            return tomorrow.strftime("%Y-%m-%d")
        if "last week" in question_lower:
            return last_week.strftime("%Y-%m-%d")
        if "next week" in question_lower:
            return next_week.strftime("%Y-%m-%d")
        if "fortnight ago" in question_lower:
            return fortnight_ago.strftime("%Y-%m-%d")
        if "fortnight later" in question_lower:
            return fortnight_later.strftime("%Y-%m-%d")
        try:
            dt = parser.parse(question, fuzzy=True)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            return None

    @classmethod
    def dprint(cls, string):
        if cls.is_print:
            print(string)
        else:
            pass







