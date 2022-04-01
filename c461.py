# 解題說明一
a, b, c = map(int, input().split())
flag = False
if a != 0:
    la = True
else:
    la = False
if b != 0:
    lb = True
else:
    lb = False
if c != 0:
    lc = True
else:
    lc = False
if (la and lb) == lc:
    print('AND')
    flag = True
if (la or lb) == lc:
    print('OR')
    flag = True
if ((la and (not lb)) or ((not la) and lb)) == lc:
    print('XOR')
    flag = True
if not flag:
    print('IMPOSSIBLE')

# 解題說明二
a, b, c = map(int, input().split())
flag = False
la = (a != 0)
lb = (b != 0)
lc = (c != 0)
if (la and lb) == lc:
    print('AND')
    flag = True
if (la or lb) == lc:
    print('OR')
    flag = True
if ((la and (not lb)) or ((not la) and lb)) == lc:
    print('XOR')
    flag = True
if not flag:
    print('IMPOSSIBLE')


# 我的解題 (以為考位元運算= =")

# def test(numbers):  # 讀入兩個數字跟邏輯運算的結果，判段經過的邏輯運算為何
#     a, b, c = map(int, numbers.split())  # a數字1，b數字2，c數字a、b邏輯運算的結果
#     res = ""  # 結果
#     if c == 1:  # 代表邏輯運算的結果是True(1)
#         if a & b:  # 如果ab兩數，皆為True
#             res = "AND"  # res = AND
#             print(res)  # 印出結果
#         if a | b:  # 如果ab兩數，其一為True
#             res = "OR"
#             print(res)
#         if a ^ b:  # 如果ab兩數互為相反(=True)
#             res = "XOR"
#             print(res)
#     elif c == 0:  # 代表邏輯運算的結果是False(0)
#         if not a & b:  # 如果ab兩數，其一不為True(=False)
#             res = "AND"
#             print(res)
#         if not a | b:  # 如果ab兩數，皆為False
#             res = "OR"
#             print(res)
#         if not a ^ b:  # 如果ab兩數，皆一致時(=False)
#             res = "XOR"
#             print(res)
#     if len(res) == 0:
#         res = "IMPOSSIBLE"
#         print(res)
#
#
# # number = input()
# # test(number)
# # input data
# input_data = ["0 0 0", "1 1 1", "3 0 1", "0 0 1"]
# # output data
# output_data = [["AND", "OR", "XOR"], ["AND", "OR"], ["OR", "XOR"], ["IMPOSSIBLE"]]
# for i in input_data:
#     test(input())
#     # print()
