fence_count = int(input())

fence_info = [int(x) for x in input().split()]
out_put = 0

if fence_info[0] == 0:
    out_put += fence_info[1]

if fence_info[-1] == 0:
    out_put += fence_info[-2]

for i in range(1, fence_count-1):
    if fence_info[i] == 0:
        out_put += min(fence_info[i+1], fence_info[i-1])


print(out_put)

# fence_count = int(input())
#
# fence_info = [int(x) for x in input().split()]
# out_put = 0
#
# for i in range(fence_count):
#     if fence_info[i] == 0 and i != (fence_count - 1) and i != 0:
#         if fence_info[i+1] > fence_info[i-1]:
#             out_put += fence_info[i-1]
#         else:
#             out_put += fence_info[i+1]
#
#     if i == 0 and fence_info[0] == 0:
#         out_put += fence_info[1]
#
#     if i == (fence_count - 1) and fence_info[-1] == 0:
#         out_put += fence_info[-2]
#
#
# print(out_put)