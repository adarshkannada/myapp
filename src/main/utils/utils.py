import calendar
import datetime


class Utils:
    def get_month_year(self):
        for i in range(1, 13):
            month = calendar.month_name[i]
            i += 1
            print(month)
            month_short_name = month[:3]
            print(month_short_name)
            today = datetime.date.today()
            year = today.year
            month_year = f"{month_short_name} {year}"
            print(month_year)


Utils().get_month_year()
