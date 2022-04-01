import sys

# num = "1JKJ'pz'{ol'{yhklthyr'vm'{ol'Jvu{yvs'Kh{h'Jvywvyh{pvu5"
#
# for i in range(100):
#     if chr(ord(num[0]) - i) =="*":
#         print(i)
#         break


for i in sys.stdin.readline().strip("\n"):
    print(chr(ord(i) - 7), end="")
