import datetime

today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
print(today)
print(tomorrow)
print(yesterday)
