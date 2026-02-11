m = int(input()) 
n = int(input()) 
perfect_square = []
for i in range(m, n+1):
    square_root = i ** 0.5 
    if square_root == int(square_root) and i == square_root ** 2:
        perfect_square.append(i) 
if len(perfect_square) == 0:
    print("No Perfect Square")
else:
    print(perfect_square[0])

     
