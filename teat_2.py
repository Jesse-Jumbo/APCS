# print(((2*2)+2)*0(2, x-1))

def G(a, x):
    if x == 0:
        return 1
    return ((2 * a) + 2) * G(a, x - 1)
    # return (a+5)*G(a-1, x-1)
    # return ((3*a)-1)*G(a, x-1)
    # return (a+6)*G(a, x-1)


'''
A.
觀察題目後，發現x-1的共同點，然後看函式內的最簡狀況是判斷x == 0，於是就:
把1帶到x，就可以忽略後面*G的地方(都是1)，然後前面的a帶入2，就剛好算出答案了
'''

data = [
    [2, 2, 2, 2, 2]
    , [0, 1, 2, 3, 4]
]

for i in range(len(data[0])):
    print(G(data[0][i], data[1][i]))
