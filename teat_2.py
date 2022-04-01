a = [1, 3, 5, 7, 9, 8, 6, 4, 2]

n = 9

tmp = 0

# for i in range(n):
#     tmp = a[i]
#     a[i] = a[n-i-1]
#     a[n-i-1] = tmp


for i in range(5):
    print(a[i], a[n-i-1])
