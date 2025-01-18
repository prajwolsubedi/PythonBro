import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12,30,0)

now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030,1,2,12,13,13)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print(f"Target date has already passed.")
else:
    print(f"Target date has not passed.")


print(now)

# print(time)
# print(today)
