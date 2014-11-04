#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

numbers = []
max_palindrome = 1
for i in range (100,999):
    for j in range(100,999):
        number = i * j
        test = str(number)
        if test == test[::-1] and number > max_palindrome:
            max_palindrome = number     

print(max_palindrome)       
        
             
