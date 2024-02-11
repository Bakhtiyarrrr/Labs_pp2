import datetime

x = datetime.datetime.today()
y = x + datetime.timedelta(days = 1)
z = (y - x).total_seconds()
print(z)

