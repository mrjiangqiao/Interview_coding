#-*-conding:utf-8-*-
in_str = input()
word_list = "abcdefghijklmnopqrstuvwxyz"
exchange_dic = {}
out_str = ""
for i in in_str:
    if i not in exchange_dic.keys():
        exchange_dic[i]= word_list[len(exchange_dic.keys())]
        out_str= out_str + exchange_dic[i]
    else:
        out_str = out_str + exchange_dic[i]
print(out_str)
