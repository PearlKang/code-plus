N=int(input())
sum=0
for n in range(1,N+1):
    sum+=N//n * n
print(sum)