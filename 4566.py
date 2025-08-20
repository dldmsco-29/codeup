a = int(input())
b = int(input())
prime_list = []

for i in range(a, b+1):
    cnt = 0
    if i < 2:
        continue
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)
    
print(sum(prime_list))
print(min(prime_list))