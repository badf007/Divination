from bs4 import BeautifulSoup
import mysql.connector
import datetime

BASE_URL = "https://www.conectate.com.do/loterias/"

dt = datetime.datetime(2021, 8, 9)
end = datetime.datetime(2011, 1, 1)
step = datetime.timedelta(days=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d'))
    dt -= step
    print("fucking prueba")
    print(dt)

print(result)
print("fucking work")