# def calculate(year):
#     year = int(year)
#     res = "平年"
#     if year % 4 == 0 and year % 100 != 0:
#         res = "閏年"
#     if year % 400 == 0:
#         res = "閏年"
#     print(res)
#
#
# try:
#     while True:
#         year = input()
#         calculate(year)
# except EOFError:
#     print("Error")
#     pass
# import sys
#
# num = int(sys.stdin.readline())
#
# res = "平年"
# if num % 4 == 0 and num % 100 != 0:
#     res = "閏年"
#     if num % 400 == 0:
#         res = "閏年"
#     print(res)
# import sys
# for i in sys.stdin:
#     num = int(i)
#     res = "平年"
#     if num % 4 == 0 and num % 100 != 0:
#         res = "閏年"
#     if num % 400 == 0:
#         res = "閏年"
#     print(res)
#
# if __name__ == "__main__":
#     while 1:
#         try:
#             year = int(input())
#         except:
#             break
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400 == 0:
#                     print("閏年")
#                 else:
#                     print("平年")
#             else:
#                 print("閏年")
#         else:
#             print("平年")
#