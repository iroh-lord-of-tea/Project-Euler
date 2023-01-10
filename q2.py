# Question 2
# Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms


# 1
# 1,2
# 1,2,3
# 1,2,3,5

f_seq = []
f_seq.append(0)
f_seq.append(1)

n = 2
while True:
    if  f_seq[n-1] < 4e6:
        if(f_seq[n-1] + f_seq[n-2] < 4e6):
            f_seq.append(f_seq[n-1] + f_seq[n-2])
            n += 1
        else:
            break
    else:
        break

print(f_seq)

