"""
string version
"""
# import sys
#
# count = 0
#
# try:
#     while True:
#         for number in sys.stdin:
#             count = 0
#             for i in range(int(number), 0, -1):
#                 if i > 10:
#                     if int(str(i)[0]) > int(str(i)[1]):
#                         continue
#                 if i > 111:
#                     if int(str(i)[1]) > int(str(i)[2]):
#                         continue
#                 if i > 1000:
#                     if int(str(i)[2]) > int(str(i)[3]):
#                         continue
#                 if i > 10000:
#                     if int(str(i)[3]) > int(str(i)[4]):
#                         continue
#                 if i > 100000:
#                     if int(str(i)[4]) > int(str(i)[5]):
#                         continue
#                 if i > 1000000:
#                     if int(str(i)[5]) > int(str(i)[6]):
#                         continue
#                 if i > 10000000:
#                     if int(str(i)[6]) > int(str(i)[7]):
#                         continue
#                 if i > 100000000:
#                     if int(str(i)[7]) > int(str(i)[8]):
#                         continue
#                 if "0" in str(i):
#                     continuenj
#                 if i == number:
#                     print(i, number)
#                     continue
#                 count += 1
#             print(count)
# except:
#     pass
#
