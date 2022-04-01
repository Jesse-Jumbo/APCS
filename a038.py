# def reverse_str(string):  # 反轉字串的函式
#     rev_str = string[::-1]  # 反轉字串
#     res_str = rev_str.lstrip("0")  # 去除前面的0
#     if res_str == "":  # 如果是空字串
#         print("0")  # 印出 0
#     else:  # 否則
#         print(res_str)  # 印出結果字串
#
#
# reverse_str(input())  # 輸入數字進入函式

def reverse_str(string):  # 反轉字串的函式
    rev_str = string[::-1]  # 反轉字串
    res_str = int(rev_str)  # 轉成整數型態(去除前面多餘的零)
    print(res_str)  # 印出結果字串


reverse_str(input())  # 輸入數字進入函式

