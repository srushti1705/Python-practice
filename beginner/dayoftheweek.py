import datetime

given_date = input("Enter date (dd/mm/yyyy): ")

date_obj = datetime.datetime.strptime(given_date, "%d/%m/%Y")

print("Day is:", date_obj.strftime("%A"))