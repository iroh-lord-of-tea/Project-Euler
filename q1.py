# Project Euler Question 1 :: Find the sum of all multiples of 3 or 5 below 1000
# Joel Sved
import numpy as np      

target = 999
sum = 0
for i in range(target+1):
    if (i%3 == 0 or i%5 == 0):
        sum = sum + i
        print(i)
print(sum)        



