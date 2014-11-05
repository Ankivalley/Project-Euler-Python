sum = 0
squares = []
x = 0
while x < 101:
    sum += x
    squares.append(x**2)
    x += 1
squared_sum = sum ** 2
for n in squares:
    squared_sum -= n
print(squared_sum)        