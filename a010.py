num = int(input())

res = {}

while True:
    for i in range(2, num + 1):
        if num % i == 0:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
            num = num // i
            break
    if num == 1:
        break

output = ""
for i in res:
    if len(res) == 1 and res[i] == 1:
        print(i)
    else:
        if res[i] == 1:
            output = f"{output}{i} * "
        else:
            output = f"{output}{i}^{res[i]} * "


print(output[:-2])

