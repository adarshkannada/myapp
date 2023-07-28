import calendar
import datetime


class Utils:
    def get_current_month_year(self):
        today = datetime.date.today()
        year = today.year
        month_number = today.month
        month = calendar.month_name[month_number]
        month_short_name = month[:3]
        month_year = f"{month_short_name} {year}"
        return month_year

    def get_month_year(self, month_number, year):
        month = calendar.month_name[month_number]
        month_short_name = month[:3]
        month_year = f"{month_short_name} {year}"
        return month_year

