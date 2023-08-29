def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

N = int(input())
a = list(map(int, input().split()))
ans = 0
for n in a:
    if isPrime(n):
        ans += 1
print(ans)