import sys

input = sys.stdin.readline

def check(password):
    ja = 0
    mo = 0

    for i in password:
        if i in 'aeiou':
            mo += 1
        else:
            ja += 1

    if ja >= 2 and mo >= 1:
        return True
    else:
        return False

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return

    if i == len(alpha):
        return

    go(n, alpha, password + alpha[i], i+1)
    go(n, alpha, password, i+1)

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()
go(L, alpha, "", 0)