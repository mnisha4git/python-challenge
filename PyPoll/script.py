import sys
import locale
import datetime

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

#print(date_format)
#'%d/%m/%Y'
today = datetime.date.today()
print(today)
#datetime.date(2012, 4, 23)

#print(today.strftime(date_format))

#row[0].strftime(date_fromat) == rev_rec["month"].strftime(date_fromat)

print(datetime.date.today().strftime("%b-%Y"))