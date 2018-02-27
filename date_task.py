from datetime import datetime, timedelta
import calendar

today_date = datetime.now()
print('Today = {}'.format(today_date))
yesterday_date = today_date - timedelta(1)
print('Yesterday = {}'.format(yesterday_date))

days_in_month = calendar.monthrange(today_date.year, today_date.month)[1]
month_ago = today_date - timedelta(days=days_in_month)
print('Month ago = {}'.format(month_ago))


#второй пункт
date_string="01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)

