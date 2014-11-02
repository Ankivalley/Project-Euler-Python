multiples = []
for i in range (1,1000):
    if i % 3 == 0:
        multiples.append(i)
    elif i % 5 == 0:
        multiples.append(i)
total = 0
filtered_multiples = []
for n in multiples:
    if n in filtered_multiples:
        del(n)
    else:
        filtered_multiples.append(n)

for N in filtered_multiples:
    total += N            
    
    
print total                
        
