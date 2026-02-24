from datetime import datetime, timedelta

D = input("Enter date (dd MMM yyyy): ") 
date_obj = datetime.strptime(D, "%d %b %Y") 

previous_day = date_obj - timedelta(days=1)
next_day = date_obj + timedelta(days=1) 

print(previous_day.strftime("%Y-%m-%d %H:%M:%S")) 
print(date_obj.strftime("%Y-%m-%d %H:%M:%S")) 
print(next_day.strftime("%Y-%m-%d %H:%M:%S"))
