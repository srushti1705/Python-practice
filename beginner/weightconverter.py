weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K or L): ")

if unit == "K":
    weight = weight*2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs"
else:
    print("Invalid unit. Please enter either K for kilograms or L for pounds.")
    exit()

print(f"Your weight is {weight}{unit}")
