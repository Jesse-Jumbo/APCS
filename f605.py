import sys

goods_count, diff = map(int, sys.stdin.readline()[:-1].split())

count = 0
coast = 0
for i in range(goods_count):
    prices = [int(x) for x in sys.stdin.readline()[:-1].split()]
    if max(prices) - min(prices) >= diff:
        count += 1
        coast += sum(prices) // 3

print(count, coast)

# import sys
#
# goods_count, diff = sys.stdin.readline()[:-1].split()
#
# count = 0
# coast = 0
# for i in range(int(goods_count)):
#     prices = [int(x) for x in sys.stdin.readline()[:-1].split()]
#     prices.sort()
#     if prices[-1] - prices[0] >= int(diff):
#         count += 1
#         coast += int(sum(prices) / 3)
#
# print(count, coast)
