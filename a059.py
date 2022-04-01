t = int(input())

cal_list = [[0] * 2 for i in range(t)]
res = []
c = 0

for i in range(t):
    cal_list[i][0] = int(input())
    cal_list[i][1] = int(input())

    for j in range(cal_list[i][0], cal_list[i][1] + 1):
        if str(float(j) ** 0.5)[-1] == "0":
            res.append(j)

    print(f"Case {i + 1}: {sum(res)}")
    res = []
