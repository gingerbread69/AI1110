outcomes = [1, 2, 3, 4, 5, 6]
prime = 0
btnum = 0
odd = 0
def isPrime(n):
    x = 1
    for i in range(1, n):
        if n % i == 0:
            x += 1
    if x == 2:
        return True
    else:
        return False

for i in outcomes:
    if i > 2 and i < 6:
        btnum += 1
    if i%2 == 1:
        odd += 1
    if isPrime(i):
        prime += 1

print(f"Probability of (i) getting an prime number: {prime/6}, (ii) getting a number between 2 and 6: {btnum/6}, (iii) getting an odd number: {odd/6}")
