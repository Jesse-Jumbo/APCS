"""
範例輸入 #1       範例輸出 #
// 第一筆測資     // 第一筆測資
3 2 3           3 2
1 1             1 1
3 1             1 3
1 2             2 1
1 0 0
// 第二筆測資     // 第二筆測資
3 2 2           2 3
3 3             2 1 3
2 1             1 2 3
1 2
0 1
"""
r, c, m = map(int, input().split())

list_b = [[0] * c for i in range(r)]

for i in range(r):
    list_b[i] = input().split()


history = input().split()

for k in history:
    if int(k) == 0:
        list_a = [[0] * len(list_b) for i in range(len(list_b[0]))]
        r = len(list_b) - 1
        c = 0
        for i in range(len(list_a)):
            for j in range(len(list_a[0])):
                list_a[i][j] = list_b[r][c]
                r -= 1
            c += 1
            r = len(list_b) - 1
        list_b = list_a
    else:
        list_b = list_b[::-1]

print(len(list_b), len(list_b[0]))
for i in list_b:
    print(*i, sep=" ")

