from datetime import datetime, timedelta

D1 = input("Enter first date (e.g. Jul 02 2000): ") 
D2 = input("Enter second date (e.g. Jul 02 2001): ")
D1 = datetime.strptime(D1, "%b %d %Y") 
D2 = datetime.strptime(D2, "%b %d %Y") 
no_of_days = (D2-D1).days
for i in range(no_of_days + 1):
    print(D1 + timedelta(days=i))