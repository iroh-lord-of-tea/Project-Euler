# Question 2
# Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
import numpy as np

f_seq = []
f_seq.append(0)
f_seq.append(1)
target_val = 4e6

n = 2
while True:
    if  f_seq[n-1] < target_val:
        if(f_seq[n-1] + f_seq[n-2] < target_val):
            f_seq.append(f_seq[n-1] + f_seq[n-2])
            n += 1
        else:
            break
    else:
        break

sum_even_nos = np.sum([num for num in f_seq if num % 2 == 0])

