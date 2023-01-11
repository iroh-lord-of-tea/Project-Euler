
# Largest prime factor


n = 600851475143 
fac = 2
primefacs = []

while fac <= n/2 + 1:
    if n % fac == 0:
        primefacs.append(fac)
        n /= fac
        fac = 2

    else:
        fac += 1
        
        
print(n)