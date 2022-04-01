import math

while True:
    try:
        a, b = map(int, input().split())
        print(math.gcd(a, b))
    except EOFError:
        break
# while True:
#     try:
#         a, b = map(int, input().split())
#
#         if a == 1 or b == 1:
#             print(1)
#             continue
#
#         if a % 2 == 0 and b % 2 == 0:
#             for i in range(min(a, b) + 2, 0, -2):
#                 if a % i == 0 and b % i == 0:
#                     print(i)
#                     break
#         else:
#             for i in range(min(a, b) + 1, 0, -2):
#                 if a % i == 0 and b % i == 0:
#                     print(i)
#                     break
#     except EOFError:
#         break