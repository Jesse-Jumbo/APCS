n, m = map(int, input().split())
num_list = [[]] * n
max_list = []

for i in range(n):
    num_list[i] = list(map(int, input().split()))
    max_num = max(num_list[i])
    max_list.append(max_num)


sum_num = sum(max_list)
print(sum_num)

out_put = ""
for i in max_list:
    if sum_num % i == 0:
        out_put += f"{i} "

if not out_put:
    print("-1")
else:
    print(out_put[:-1])


