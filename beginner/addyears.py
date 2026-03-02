from datetime import datetime, timedelta 

D1 = input("Enter date (e.g. Jul 02 2000): ") 
Y = int(input("Enter the number of years to add: "))  
date_obj = datetime.strptime(D1, "%b %d %Y") 
D2 = date_obj + timedelta(days=Y*365) 
print(D2)
