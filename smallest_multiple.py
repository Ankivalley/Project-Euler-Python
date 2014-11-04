n = 2511
total = 0
while n > 0:
    for i in range(1,20):
        if n % i == 0:
            total += 1
        else:
            total = 0
            n += 1
    if total > 19:
        break
        
print(n)                    
            
            
            