good_1, good_2 = map(int, input().split())  # 買進產品1、2
_good_1, _good_2 = good_1 * -1, good_2 * -1  # 退回產品1、2

good_one = 0  # 記錄產品1在一個購物車被放入的次數
good_two = 0  # 記錄產品2在一個購物車被放入的次數
_good_one = 0  # 記錄產品1在一個購物車被退回的次數
_good_two = 0  # 記錄產品2在一個購物車被退回的次數

goods = []

visits = int(input())  # 客人數量

records = []  # 購物車紀錄

for i in range(visits):  # 根據客人數量決定紀錄幾次
    records.append([int(x) for x in input().split()])  # 用list分別儲存每個客人的購物紀錄

for record in records:  # 獲取單個客人的購物紀錄
    good_one = record.count(good_1)  # 計算買進產品1的次數
    _good_one = record.count(_good_1)  # 計算退回產品1的次數
    good_two = record.count(good_2)  # 計算買進產品2的次數
    _good_two = record.count(_good_2)  # 計算退回產品2的次數
    goods.append(min([good_one - _good_one, good_two - _good_two]))  # 紀錄從買進產品1和2中挑選最少的(代表兩個都有買)

print(sum(goods))  # 把每個客人買進商品的數量相加

# 解答2
a, b = map(int, input().split())
t = int(input())
ans = 0
for i in range(t):
    l = [int(x) for x in input().split()]
    na = l.count(a) - l.count(-a)
    nb = l.count(b) - l.count(-b)
    if na > 0 and nb > 0:
        ans += 1

print(ans)

# 解答1
a, b = map(int, input().split())
t = int(input())
ans = 0
for i in range(t):
    l = [int(x) for x in input().split()]
    na = 0
    nb = 0
    for x in l:
        if x == a:
            na += 1
        elif x == -a:
            na -= 1
        elif x == b:
            nb += 1
        elif x == -b:
            nb -= 1
    if na > 0 and nb > 0:
        ans += 1
