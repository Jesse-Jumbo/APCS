"""
https://zerojudge.tw/ShowProblem?problemid=c294
原題pdf檔 https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnx6c2dpdGl0aXR8Z3g6NTRkNzUxYTBkMmNjYTZmOA
"""


def test(three_number):
    numbers_list = []
    list = three_number.split()
    for i in list:
        numbers_list.append(int(i))
    numbers_list.sort()
    a = numbers_list[0]
    b = numbers_list[1]
    c = numbers_list[2]
    if a + b <= c:
        res = "No"
    elif a * a + b * b < c * c:
        res = "Obtuse"
    elif a * a + b * b == c * c:
        res = "Right"
    elif a * a + b * b > c * c:
        res = "Acute"

    print(a, b,  c)
    print(res)

numbers = "4 5 6"
test(numbers)
