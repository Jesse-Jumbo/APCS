'''
參考資料: https://dreamisadream97.pixnet.net/blog/post/165781698-n%E5%80%8B%E5%B9%B3%E9%9D%A2%E6%9C%80%E5%A4%9A%E5%8F%AF%E5%88%87%E5%87%BA%E5%B9%BE%E5%80%8B%E7%A9%BA%E9%96%93
'''
import sys
"""
B. 11
70~79(會進入s>60的if語塊，變成D等) + 60(因為==60，會進入else語塊，變成F等)
"""

def test(n):
    if n == 1:
        return 2
    return test(n - 1) + test2(n - 1)


def test2(n):
    if n == 1:
        return 2
    return test2(n - 1) + n


try:
    for n in sys.stdin.readlines():
        n = int(n)
        print(int((n * (n * n + 5) / 6) + 1))
except ValueError:
    pass
