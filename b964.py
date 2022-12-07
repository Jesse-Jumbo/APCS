no = input()
input_list = sorted(map(int, input().split()))
best = -1
worst = 101

print(*input_list, sep=" ")

for i in input_list:
    if 60 > i > best:
        best = i
    if worst > i > 59:
        worst = i

print("best case") if best == -1 else print(best)
print("worst case", end="") if worst == 101 else print(worst, end="")
