# Project Euler Question 1 :: Find the sum of all multiples of 3 or 5 below 1000
# Joel Sved
import numpy as np 

num_arr = np.arange(1,1001)
multiples_list = []

for i in range(len(num_arr)):
    if (i%3 == 0 or i%5 == 0):
        multiples_list = np.append(multiples_list,i)
        print(i)
print(np.sum(multiples_list))        



