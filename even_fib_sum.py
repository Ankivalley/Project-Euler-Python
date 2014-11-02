Fibonacci = [1,2] 

count = 0
new_n = 0
while new_n < 4000000:
    new_n = Fibonacci[count] + Fibonacci[count + 1]
    Fibonacci.append(new_n)
    count += 1

even_fibs = []       
for n in Fibonacci:
    if n % 2 == 0:
        even_fibs.append(n)
    else:
        del(n)

total = 0
for N in even_fibs:
    total += N

print(total)   
 


                        
