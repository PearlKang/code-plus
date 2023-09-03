import sys

input = sys.stdin.readline

inf = -10**9
n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
ans = 0

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

def go(day, s):
    global ans
    if day == n + 1:
        ans = max(ans, s)
        return
    if day > n + 1:
        return
    go(day + 1, s)
    go(day + t[day], s + p[day])

go(1, 0)
print(ans)