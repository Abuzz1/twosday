import datetime
import calendar

class Twosday():
    def check(year): # check a year function
        def day(month, day, year): # check the day of the week.
            value = datetime.date(year, month, day)
            alpha = value.weekday()
            day = calendar.day_name[alpha]
            return day

        def check_month(month): # check the if there is a twosday in a given month.
            for i in range(1, 31):
                try:
                    a = day(month, i, year)
                    if a == "Tuesday" and month == 2 and i == 22 and abs(year%100) == 22:
                        print("="*10)
                        print(f"Year {year}: Twosday  >")

                except ValueError:
                    pass

        for i in range(1, 12): # check the year by going through each month.
            check_month(i)
