import re
def change1(str1):
    row = int(str1.split("C")[0].strip("R"))
    col = int(str1.split("C")[1])
    col_word = ""
    while(1):
        div_cur = col//26
        rema = col % 26
        if rema>0:
            col_word = chr(64+rema) + col_word
        if rema==0 and div_cur>0:
            col_word = "Z"+col_word
            div_cur =div_cur - 1
        if div_cur >0:
            col = div_cur
        else:
            break
    result_str = col_word + str(row)
    return result_str

def change2(str2):
    row = re.search("\d+",str2).group()
    col = re.search("[A-Z]+", str2).group()
    ex = len(col)
    col_num = 0
    for i in col:
        ex = ex - 1
        col_num += (ord(i) - 64) * 26 ** ex
    result_str = "R"+row+"C"+str(col_num)
    return result_str

T = int(input())
test_list = []
for i in range(T):
    test_list.append(input())
for test_exam in test_list:
    if re.match(r"R\d+C\d+",test_exam) is not None:
        print(change1(test_exam))
    else:
        print(change2(test_exam))