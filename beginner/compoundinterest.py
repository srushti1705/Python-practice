principle = 0
rate = 0 
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Invalid input. Please enter a positive value for the principle.")

while rate <= 0 or rate > 100:
    rate = float(input("Enter the annual interest rate: "))
    if rate <= 0 or rate > 100:
        print("Invalid input. Please enter a value between 1 and 100 for the interest rate.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Invalid input. Please enter a positive value for the time period.")

total = principle*pow((1+rate)/100, time)

print(f"Balance after {time} year/s will be {total : .2f}")