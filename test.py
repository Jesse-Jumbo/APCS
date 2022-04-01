import sys

times = int(input())
ans = {}
for i in range(times):
    res = 0
    num = ""
    for j in sys.stdin.readline()[:-1]:
        num = f"{num}{j}"
        res += int(j)

    ans[num] = res

sum_num = 0

max_value = max(ans.values())

for key, value in ans.items():
    if value == max_value:
        print(key)
        print(value)
        break

