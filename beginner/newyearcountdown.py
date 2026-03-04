from datetime import datetime

D = input("Enter a date and time (e.g., Jan 1 2023 12:00 PM): ") 
D_obj = datetime.strptime(D, "%b %d %Y %I:%M %p") 
year = D_obj.year
next_year = datetime(year+1, 1, 1)
time_left_for_next_year = next_year - D_obj
hours = time_left_for_next_year.days * 24 + time_left_for_next_year.seconds // 3600
minutes = (time_left_for_next_year.seconds % 3600) // 60
print(hours, "hours", minutes, "minutes")
