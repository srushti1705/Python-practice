food = []
prices = []
total = 0 

while True:
    food_item = input("Enter a food to buy (q to quit): ")
    if food_item.lower() == 'q':  # Use 'q' as a string
        break 
    else: 
        price = float(input(f"Enter the price of {food_item}: $"))
        food.append(food_item)  # Append food_item, not food
        prices.append(price) 

print("YOUR CART")

for food_item in food:
    print(food_item)

for price in prices:
    total += price

print(f"Total: ${total}")