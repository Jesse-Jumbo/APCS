import sys  # 想測試更快的速度而已

length = int(input())

for i in range(length):  # 根據輸入的第一個數字，決定程式執行的次數
    # for i in sys.stdin:
    #     cal_list = list(map(int, i.split()))
    cal_list = list(map(int, input().split()))  # 將輸入的數字列，用空格分隔，並依序轉換成數字，存在list裡
    a_1 = cal_list[0]  # 獲取list中的a1
    a_2 = cal_list[1]  # 獲取list中的a2
    d = a_2 - a_1  # 後項減前項，獲取公差
    if cal_list[-1] == cal_list[0] + (len(cal_list) - 1) * d:  # 判斷等差公式：an = a1 + (n - 1)*d
        cal_list.append(cal_list[-1] + d)  # 在list尾加上第n+1項(an+d)
    else:  # 否則(等比數列)
        d = (a_2 // a_1)  # 獲取前項除後項的商
        cal_list.append((cal_list[-1] * d))  # 在list尾加上第n+1項(an*d)

    for i in cal_list:  # 迭代list中的每個項目
        print(i, end=" ")  # print出來，並用一個空格相隔
    print()  # 結束後換行
