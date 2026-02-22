import datetime 

date_str = input("Enter a date (dd/mm/yyyy): ") 
datetime_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y") 
year = datetime_obj.year 

last_day_obj = datetime.datetime(year, 12, 31) 

duration = last_day_obj - datetime_obj
print(duration)