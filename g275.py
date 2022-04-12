import sys

times = int(sys.stdin.readline()[:-1])


for i in range(times):
    st_sentence = sys.stdin.readline()[:-1].split()
    nd_sentence = sys.stdin.readline()[:-1].split()
    is_illegal = False
    output = ""
    if st_sentence[1] == st_sentence[3] or nd_sentence[1] == nd_sentence[3] or st_sentence[1] != st_sentence[5] or nd_sentence[1] != nd_sentence[5]:
        output = f"{output}A"

    if st_sentence[-1] != "1" or nd_sentence[-1] != "0":
        output = f"{output}B"

    if st_sentence[1] == nd_sentence[1] or st_sentence[3] == nd_sentence[3] or st_sentence[5] == nd_sentence[5]:
        output = f"{output}C"

    if not output:
        print("None")
    else:
        print(output)
