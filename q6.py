# Question 6
# Joel Sved

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sqr_sum = []
sum_sqr = []

for i in range(101):
    sqr_sum.append(i)
    sum_sqr.append(i*i)

num_arr = sum(sqr_sum)**2 - sum(sum_sqr)
print(num_arr)