from datetime import datetime 

date = input("Enter date (e.g. 02 Jul 2000): ") 
date_str = "%d %b %Y"
date_obj = datetime.strptime(date, date_str)
day = date_obj.strftime("%A") 
print(day)