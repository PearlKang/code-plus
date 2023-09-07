import sys

input = sys.stdin.readline

N, S = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, (1 << N)):
    # s = sum(a[k] for k in range(N) if (i & (1 << k) > 0))
    s = 0

    for k in range(N):
        if (i & (1 << k) > 0):
            s += a[k]

    if S == s:
        ans += 1

print(ans)