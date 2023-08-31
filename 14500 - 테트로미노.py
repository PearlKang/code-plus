blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1)),
)

N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        for block in blocks:
            ok = True
            s = a[i][j]

            for dx, dy in block:
                x, y = i + dx, j + dy

                if 0 <= x < N and 0 <= y < M:
                    s += a[x][y]
                else:
                    ok = False
                    break

            if ok and ans < s:
                ans = s
print(ans)