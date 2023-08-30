array = [int(input()) for _ in range(9)]
array.sort()
sum = sum(array)
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if sum-array[i]-array[j] == 100:
            del array[j]
            del array[i]
            for k in range(len(array)):
                print(array[k])
            exit()
